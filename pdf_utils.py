from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(suggestions: str) -> BytesIO:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    text = pdf.beginText(40, 800)
    text.setFont("Helvetica", 12)
    for line in suggestions.splitlines():
        text.textLine(line)
    pdf.drawText(text)
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
