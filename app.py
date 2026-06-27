from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_file,
    url_for,
    flash
)

from datetime import datetime
import socket
import ipaddress

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
    UserMixin
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database.queries import (
    create_user,
    get_user,
    get_user_by_id,
    save_scan,
    save_port_result,
    get_scan_history,
    get_scan_by_id,
)

from scanner.scanner_engine import run_scan
from reports.report_manager import generate_reports
from fixes.repeat_scan import repeat_scan
from scanner.host_discovery import discover_hosts


app = Flask(__name__)

app.secret_key = "super_secret_key"


# ==========================================
# Flask Login
# ==========================================

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"


class User(UserMixin):

    def __init__(
            self,
            id,
            username,
            email,
            password):

        self.id = id
        self.username = username
        self.email = email
        self.password = password


@login_manager.user_loader
def load_user(user_id):

    user_data = get_user_by_id(int(user_id))

    if user_data:

        return User(
            user_data["id"],
            user_data["username"],
            user_data["email"],
            user_data["password"]
        )

    return None


# ==========================================
# Validation
# ==========================================

def is_valid_target(target):

    # Accept CIDR networks
    try:

        ipaddress.ip_network(target, strict=False)

        return True

    except ValueError:

        pass

    # Accept single IPs and hostnames
    try:

        socket.gethostbyname(target)

        return True

    except socket.error:

        return False


# ==========================================
# HOME
# ==========================================

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        target = request.form["target"]

        scan_type = request.form["scan_type"]

        if not is_valid_target(target):

            flash("Invalid IP address or hostname")

            return redirect("/")

        if scan_type == "network":

            hosts = discover_hosts(target)

            return render_template(

                "network_results.html",

                target=target,

                 hosts=hosts

             )
        results = run_scan(target)

        scan_id = None

        # save reports only for logged in users
        if current_user.is_authenticated:

            reports = generate_reports(
                target,
                results
            )

            scan_id = save_scan(

                target,

                str(datetime.now()),

                reports["txt_path"],

                reports["pdf_path"],

                current_user.id
            )

            for port, details in results.items():

                save_port_result(

                    port,

                    details["state"],

                    details["service"],

                    details["version"],

                    details["risk"],

                    details["recommendation"],

                    scan_id
                )

        return render_template(

            "result.html",

            results=results,

            target=target,

            scan_id=scan_id
        )

    return render_template("index.html")


# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        confirm_password = request.form[ "confirm_password" ] # Password check 
        if password != confirm_password: 
            flash( "Passwords do not match" ) 
            return redirect( "/register" )

        existing_user = get_user(username)

        if existing_user:

            flash("Username already exists")

            return redirect("/register")

        hashed_password = generate_password_hash(
            password
        )

        create_user(

            username,

            email,

            hashed_password
        )

        flash("Registration successful")

        return redirect("/login")

    return render_template("register.html")


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = get_user(username)

        if user and check_password_hash(
                user["password"],
                password):

            logged_user = User(

                user["id"],

                user["username"],

                user["email"],

                user["password"]
            )

            login_user(logged_user)

            return redirect("/")

        flash("Invalid username or password")

    return render_template("login.html")


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/")


# ==========================================
# HISTORY
# ==========================================

@app.route("/history")
@login_required
def history():

    scans = get_scan_history(
        current_user.id
    )

    return render_template(

        "history.html",

        scans=scans
    )


# ==========================================
# DOWNLOAD TXT
# ==========================================

@app.route("/download_txt/<int:scan_id>")
@login_required
def download_txt(scan_id):

    scan = get_scan_by_id(scan_id)

    return send_file(

        scan["txt_report_path"],

        as_attachment=True
    )


# ==========================================
# DOWNLOAD PDF
# ==========================================

@app.route("/download_pdf/<int:scan_id>")
@login_required
def download_pdf(scan_id):

    scan = get_scan_by_id(scan_id)

    return send_file(

        scan["pdf_report_path"],

        as_attachment=True
    )

# ==========================================
# REPEAT SCAN
# ==========================================

@app.route("/repeat_scan", methods=["POST"])
@login_required
def repeat_port_scan():

    ip = request.form["ip"]

    port = int(

        request.form["port"]

    )

    result = repeat_scan(

        ip,

        port

    )

    return render_template(

        "repeat_result.html",

        result=result,

        ip=ip

    )


@app.route("/view_txt/<int:scan_id>")
@login_required
def view_txt_report(scan_id):

    scan = get_scan_by_id(scan_id)

    with open(scan["txt_report_path"], "r") as file:

        content = file.read()

    return render_template(
        "txt_report_view.html",
        target=scan["target"],
        content=content
    )

from flask import send_file


@app.route("/view_pdf/<int:scan_id>")
@login_required
def view_pdf_report(scan_id):

    scan = get_scan_by_id(scan_id)

    return send_file(
        scan["pdf_report_path"],
        mimetype="application/pdf"
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )