from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def generate_resume(filename):
    # Define the PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    flowables = []

    # Title / Name
    title_style = ParagraphStyle(
        'title_style',
        parent=styles['Heading1'],
        fontSize=24,
        leading=28,
        spaceAfter=10,
        alignment=1,
    )
    flowables.append(Paragraph("Your Name", title_style))

    # Contact Information
    contact_info = "Email: your.email@example.com | Phone: (123) 456-7890 | LinkedIn: linkedin.com/in/yourprofile"
    flowables.append(Paragraph(contact_info, styles['Normal']))
    flowables.append(Spacer(1, 20))

    # Section Style
    section_style = ParagraphStyle(
        'section_style',
        parent=styles['Heading2'],
        fontSize=14,
        leading=16,
        spaceAfter=6,
        textColor=colors.black
    )

    # Subsection (Job/Education) Style
    subsection_style = ParagraphStyle(
        'subsection_style',
        parent=styles['Heading3'],
        fontSize=12,
        leading=14,
        spaceAfter=4
    )

    # Body Text Style
    body_style = ParagraphStyle(
        'body_style',
        parent=styles['BodyText'],
        fontSize=10,
        leading=12,
        spaceAfter=6
    )

    # Experience Section
    flowables.append(Paragraph("Experience", section_style))

    experiences = [
        {"title": "Job Title 1", "company": "Company 1", "dates": "Month YYYY - Month YYYY", "details": ["Responsibility 1", "Responsibility 2"]},
        {"title": "Job Title 2", "company": "Company 2", "dates": "Month YYYY - Present", "details": ["Responsibility 1", "Responsibility 2"]}
    ]

    for exp in experiences:
        flowables.append(Paragraph(f"{exp['title']} at {exp['company']} — {exp['dates']}", subsection_style))
        for detail in exp["details"]:
            flowables.append(Paragraph(f"• {detail}", body_style))
        flowables.append(Spacer(1, 8))

    # Education Section
    flowables.append(Paragraph("Education", section_style))

    education = [
        {"degree": "Bachelor of Science in Major", "school": "University Name", "dates": "Month YYYY - Month YYYY"},
        {"degree": "Master of Science in Major", "school": "University Name", "dates": "Month YYYY - Month YYYY"}
    ]

    for edu in education:
        flowables.append(Paragraph(f"{edu['degree']} from {edu['school']} — {edu['dates']}", subsection_style))
        flowables.append(Spacer(1, 8))

    # Skills Section
    flowables.append(Paragraph("Skills", section_style))

    skills = [
        ["Programming Languages", "Python, Java, C++"],
        ["Frameworks", "Django, Flask, React"],
        ["Tools", "Git, Docker, Kubernetes"]
    ]

    skill_table = Table(skills, colWidths=[120, 300])
    skill_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    flowables.append(skill_table)

    # Generate PDF
    doc.build(flowables)

if __name__ == "__main__":
    generate_resume("resume.pdf")