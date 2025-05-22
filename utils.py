import re
import json
from flask import Response
from fpdf import FPDF

def detect_ioc_type(ioc):
    patterns = {
        'ip': r'^\b(?:\d{1,3}\.){3}\d{1,3}\b$',
        'url': r'^(https?://)?[\w.-]+(?:\.[\w\.-]+)+[/#?]?.*$',
        'domain': r'^([\w.-]+)\.([a-z\.]{2,6})$',
        'hash': r'^[A-Fa-f0-9]{32}$|^[A-Fa-f0-9]{40}$|^[A-Fa-f0-9]{64}$'
    }
    for ioc_type, pattern in patterns.items():
        if re.match(pattern, ioc):
            return ioc_type
    return 'unknown'

def export_json(results):
    return Response(json.dumps(results, indent=2), mimetype='application/json')

def export_pdf(ioc, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Wyniki analizy IOC: {ioc}", ln=True)

    for name, result in results.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt=name, ln=True)
        pdf.set_font("Arial", size=10)
        json_text = json.dumps(result, indent=2, ensure_ascii=False)
        for line in json_text.split("\n"):
            pdf.multi_cell(0, 5, line)
    response = Response(pdf.output(dest='S').encode('latin1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename="{ioc}_report.pdf"'
    return response
