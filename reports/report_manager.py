from datetime import datetime

from reports.txt_report import (
    generate_txt_report
)

from reports.pdf_report import (
    generate_pdf_report
)


def generate_reports(
        target,
        scan_data):

    txt_path = generate_txt_report(
        target,
        scan_data
    )

    pdf_path = datetime.now().strftime(
        "generated_reports/pdf/report_%Y%m%d_%H%M%S.pdf"
    )

    generate_pdf_report(
        target,
        scan_data,
        pdf_path
    )

    return {

        "txt_path":
        txt_path,

        "pdf_path":
        pdf_path
    }