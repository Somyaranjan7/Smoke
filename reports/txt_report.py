from datetime import datetime


def generate_txt_report(target, scan_data):

    filename = datetime.now().strftime(
        "generated_reports/txt/report_%Y%m%d_%H%M%S.txt"
    )

    with open(filename, "w") as file:

        file.write(f"Target : {target}\n\n")

        for port, details in scan_data.items():

            file.write(
                f"Port : {port}\n"
            )

            file.write(
                f"Service : {details['service']}\n"
            )

            file.write(
                f"Risk : {details['risk']}\n"
            )

            if details["recommendation"]:

                file.write(

                details["recommendation"]

                + "\n"

                )

    return filename