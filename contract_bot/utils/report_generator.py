from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(results, filename="contract_report.pdf"):

    styles = getSampleStyleSheet()
    elements = []

    doc = SimpleDocTemplate(filename)

    for r in results:
        text = f"""
        Risk: {r['risk']} <br/>
        Type: {r['type']} <br/>
        Clause: {r['clause']} <br/><br/>
        Explanation: {r['explanation']} <br/><br/>
        """

        elements.append(Paragraph(text, styles["BodyText"]))
        elements.append(Spacer(1, 20))

    doc.build(elements)

    return filename
