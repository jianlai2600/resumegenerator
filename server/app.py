from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from jinja2 import Template
import os
import subprocess

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

TEMPLATE_PATH = 'templates/resume_template.tex'
OUTPUT_PATH = 'output/resume.pdf'

# Handle PDF generation with POST, and serve the PDF with GET
@app.route('/generate_resume', methods=['POST', 'GET'])
def generate_resume():
    if request.method == 'POST':
        # Extract data from the request
        data = request.json
        name = data.get('name', 'N/A')
        contact = data.get('contact', 'N/A')
        education = data.get('education', 'N/A')
        experiences = data.get('experiences', [])
        skills = data.get('skills', [])

        # Read and render LaTeX template
        with open(TEMPLATE_PATH, 'r') as file:
            latex_template = file.read()
        template = Template(latex_template)
        rendered_latex = template.render(name=name, contact=contact, education=education, experiences=experiences, skills=skills)

        # Write the rendered LaTeX to a temporary .tex file
        with open('output/resume.tex', 'w') as file:
            file.write(rendered_latex)

        # Compile the LaTeX file to PDF using pdflatex
        try:
            subprocess.run(['pdflatex', '-output-directory', 'output', 'output/resume.tex'], check=True)
        except subprocess.CalledProcessError:
            return jsonify({"error": "PDF generation failed"}), 500

        # Successfully generated PDF
        return jsonify({"message": "Resume generated successfully"}), 200

    elif request.method == 'GET':
        # Serve the generated PDF file
        return send_file(OUTPUT_PATH, as_attachment=False, download_name='resume.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    if not os.path.exists('output'):
        os.makedirs('output')
    app.run(debug=True)
