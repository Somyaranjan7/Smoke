from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.units import inch


def generate_pdf_report(
        target,
        scan_data,
        filename):

    document = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            f"Vulnerability Scan Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(
            1,
            0.2 * inch
        )
    )

    elements.append(
        Paragraph(
            f"Target: {target}",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(
            1,
            0.3 * inch
        )
    )

    # Port details
    for port, details in scan_data.items():

        text = (

            f"<b>Port:</b> {port}<br/>"

            f"<b>State:</b> {details['state']}<br/>"

            f"<b>Service:</b> {details['service']}<br/>"

            f"<b>Version:</b> {details['version']}<br/>"

            f"<b>Risk Level:</b> {details['risk']}<br/>"
        )

        # Only show explanation and recommendation
        # for open ports
        if details["recommendation"]:

            recommendation_lines = (
                details["recommendation"]
                .replace("\n", "<br/>")
            )

            text += (

                "<br/>"

                f"{recommendation_lines}"

            )

        text += "<br/><br/>"

        elements.append(

            Paragraph(

                text,

                styles["BodyText"]

            )

        )

    document.build(
        elements
    )

    return filename