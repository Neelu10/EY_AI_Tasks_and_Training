from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import datetime

def generate_pdf(data):
    filename = f"Health_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    # Create PDF object
    pdf = SimpleDocTemplate(filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Title style
    title_style = ParagraphStyle(
        name="Title",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=20
    )

    # Section header style
    header_style = ParagraphStyle(
        name="Header",
        parent=styles["Heading2"],
        fontSize=14,
        spaceAfter=8,
        textColor="#0B3D91"
    )

    # Body text style
    body_style = styles["BodyText"]
    body_style.fontSize = 12
    body_style.leading = 16

    elements = []

    # Add Title
    elements.append(Paragraph("🩺 AI Health & Diet Analysis Report", title_style))
    elements.append(Paragraph(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", body_style))
    elements.append(Spacer(1, 20))

    # Add each section cleanly
    for key, value in data.items():
        elements.append(Paragraph(key.replace("_", " ").title(), header_style))
        elements.append(Paragraph(str(value).replace("\n", "<br/>"), body_style))
        elements.append(Spacer(1, 12))

    pdf.build(elements)
    return filename
