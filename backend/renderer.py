from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image, Table, TableStyle, Frame

# Sample data dictionary
resume_data = {
    "name": "Jack Sparrow",
    "title": "Captain",
    "contact_info": {
        "email": "jack@sparrow.org",
        "twitter": "@sparrow",
        "phone": "0099/333 5647380",
        "location": "Tortuga"
    },
    "about_me": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus.",
    "personal": {
        "nationality": "English",
        "born": "1690"
    },
    "specializations": ["Privateering", "Buccaneering", "Parler", "Rum"],
    "interests": ["R / Android / Linux"],
    "experience": [
        {"role": "Captain of the Black Pearl", "lead": "East Indies", "years": "2018–2021", "details": "Finally got the ship back."},
        {"role": "Captain of the Black Pearl", "lead": "Tortuga", "years": "2016–2017", "details": "Lost the ship, found treasure."}
    ],
    "education": [
        {"degree": "Captain", "institution": "Tortuga Uni", "year": "1710"},
        {"degree": "Buccaneering", "institution": "M.A. London", "year": "1715"},
        {"degree": "Buccaneering", "institution": "B.A. London", "year": "1720"}
    ],
    "programming_skills": {
        "html_css": 80,
        "latex": 70,
        "python": 90,
        "r": 60,
        "javascript": 50
    },
    "languages": {
        "English": "C2",
        "French": "C2",
        "Spanish": "C2",
        "Italian": "C2"
    },
    "certificates": [
        {"title": "Captain's Certificate", "year": "1708"},
        {"title": "Travel Grant", "year": "1710"}
    ],
    "talks": [
        {"title": "How I lost my ship", "event": "Annual Pirate's Conference", "year": "Nov. 1726"}
    ]
}

def create_resume_pdf(filename, data):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="ResumeTitle", fontSize=26, leading=30, fontName="Helvetica-Bold", textColor=colors.black, spaceAfter=10))
    styles.add(ParagraphStyle(name="Subtitle", fontSize=16, leading=18, textColor=colors.black, spaceAfter=12))
    styles.add(ParagraphStyle(name="SectionHeading", fontSize=14, leading=18, textColor=colors.black, spaceAfter=10))
    styles.add(ParagraphStyle(name="NormalText", fontSize=10, leading=12, textColor=colors.black, spaceAfter=6))

    # Header
    elements.append(Paragraph(data['name'], styles['ResumeTitle']))
    elements.append(Paragraph(data['title'], styles['Subtitle']))

    # Contact Information
    contact_info = f"{data['contact_info']['email']} | {data['contact_info']['twitter']} | {data['contact_info']['phone']} | {data['contact_info']['location']}"
    elements.append(Paragraph(contact_info, styles['NormalText']))

    # About Me
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("About Me", styles['SectionHeading']))
    elements.append(Paragraph(data['about_me'], styles['NormalText']))

    # Personal Details
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Personal", styles['SectionHeading']))
    elements.append(Paragraph(f"Nationality: {data['personal']['nationality']}", styles['NormalText']))
    elements.append(Paragraph(f"Born: {data['personal']['born']}", styles['NormalText']))

    # Areas of Specialization
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Areas of Specialization", styles['SectionHeading']))
    for specialization in data['specializations']:
        elements.append(Paragraph(f"- {specialization}", styles['NormalText']))

    # Experience
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Experience", styles['SectionHeading']))
    for exp in data['experience']:
        elements.append(Paragraph(f"{exp['years']} - {exp['role']} at {exp['lead']}", styles['NormalText']))
        elements.append(Paragraph(exp['details'], styles['NormalText']))

    # Education
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Education", styles['SectionHeading']))
    for edu in data['education']:
        elements.append(Paragraph(f"{edu['year']} - {edu['degree']} at {edu['institution']}", styles['NormalText']))

    # Programming Skills with Progress Bars
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Programming Skills", styles['SectionHeading']))
    for skill, level in data['programming_skills'].items():
        elements.append(Paragraph(f"{skill}: {'█' * (level // 10)} {level}%", styles['NormalText']))

    # Languages
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Languages", styles['SectionHeading']))
    for lang, proficiency in data['languages'].items():
        elements.append(Paragraph(f"{lang}: {proficiency}", styles['NormalText']))

    # Certificates & Grants
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Certificates & Grants", styles['SectionHeading']))
    for cert in data['certificates']:
        elements.append(Paragraph(f"{cert['year']} - {cert['title']}", styles['NormalText']))

    # Talks
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Talks", styles['SectionHeading']))
    for talk in data['talks']:
        elements.append(Paragraph(f"{talk['year']} - {talk['title']} at {talk['event']}", styles['NormalText']))

    # Build PDF
    doc.build(elements)

# Generate the PDF
create_resume_pdf("resume_output.pdf", resume_data)