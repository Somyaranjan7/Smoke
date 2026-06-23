from database.db import get_connection


# ==========================
# USER FUNCTIONS
# ==========================

def create_user(username, email, password):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    INSERT INTO user(
        username,
        email,
        password
    )

    VALUES(%s,%s,%s)

    """

    cursor.execute(

        sql,

        (
            username,
            email,
            password
        )
    )

    connection.commit()

    connection.close()


def get_user(username):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    SELECT *

    FROM user

    WHERE username=%s

    """

    cursor.execute(

        sql,

        (username,)
    )

    user = cursor.fetchone()

    connection.close()

    return user


def get_user_by_id(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    SELECT *

    FROM user

    WHERE id=%s

    """

    cursor.execute(

        sql,

        (user_id,)
    )

    user = cursor.fetchone()

    connection.close()

    return user


# ==========================
# SCAN HISTORY
# ==========================

def save_scan(
        target,
        scan_time,
        txt_path,
        pdf_path,
        user_id):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    INSERT INTO scan_history(

        target,
        scan_time,
        txt_report_path,
        pdf_report_path,
        user_id

    )

    VALUES(%s,%s,%s,%s,%s)

    """

    cursor.execute(

        sql,

        (
            target,
            scan_time,
            txt_path,
            pdf_path,
            user_id
        )
    )

    connection.commit()

    scan_id = cursor.lastrowid

    connection.close()

    return scan_id


def get_scan_history(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    SELECT *

    FROM scan_history

    WHERE user_id=%s

    ORDER BY id DESC

    """

    cursor.execute(

        sql,

        (user_id,)
    )

    scans = cursor.fetchall()

    connection.close()

    return scans


def get_scan_by_id(scan_id):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    SELECT *

    FROM scan_history

    WHERE id=%s

    """

    cursor.execute(

        sql,

        (scan_id,)
    )

    scan = cursor.fetchone()

    connection.close()

    return scan


# ==========================
# PORT RESULTS
# ==========================

def save_port_result(
        port,
        state,
        service,
        version,
        risk,
        recommendation,
        scan_id):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    INSERT INTO port_result(

        port,
        state,
        service,
        version,
        risk,
        recommendation,
        scan_id

    )

    VALUES(%s,%s,%s,%s,%s,%s,%s)

    """

    cursor.execute(

        sql,

        (
            port,
            state,
            service,
            version,
            risk,
            recommendation,
            scan_id
        )
    )

    connection.commit()

    connection.close()


def get_port_results(scan_id):

    connection = get_connection()
    cursor = connection.cursor()

    sql = """

    SELECT *

    FROM port_result

    WHERE scan_id=%s

    """

    cursor.execute(

        sql,

        (scan_id,)
    )

    ports = cursor.fetchall()

    connection.close()

    return ports


def get_scan_by_id(scan_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT *
        FROM scan_history
        WHERE id=%s
        """,

        (scan_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result