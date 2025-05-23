from flask import Flask, render_template, request, jsonify, send_file
import importlib
import os
from config import DEFAULT_ANALYZERS
from utils import detect_ioc_type, export_json, export_pdf
from ollama_client import ask_llm

app = Flask(__name__)
ANALYZERS_PATH = 'analyzers'

def load_analyzers(ioc_type):
    analyzers = {}
    for fname in os.listdir(ANALYZERS_PATH):
        if not fname.endswith(".py") or fname.startswith("__"):
            continue
        name = fname.replace("_analyzer.py", "").replace(".py", "")
        module = importlib.import_module(f"{ANALYZERS_PATH}.{fname[:-3]}")
        clsname = [c for c in dir(module) if c.endswith("Analyzer")][0]
        analyzer = getattr(module, clsname)()
        analyzers[name] = analyzer
    return analyzers

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ioc = request.form["ioc"]
        ioc_type = detect_ioc_type(ioc)
        analyzers = load_analyzers(ioc_type)
        results = {}
        for name, analyzer in analyzers.items():
            try:
                results[name] = analyzer.analyze(ioc)
            except Exception as e:
                results[name] = {"error": str(e)}
        rec = ask_llm(ioc, results)
        return render_template("results.html", ioc=ioc, results=results, rec=rec)
    return render_template("index.html")

@app.route("/api/<path:ioc>")
def api_result(ioc):
    ioc_type = detect_ioc_type(ioc)
    analyzers = load_analyzers(ioc_type)
    results = {}
    for name, analyzer in analyzers.items():
        try:
            results[name] = analyzer.analyze(ioc)
        except Exception as e:
            results[name] = {"error": str(e)}
    return export_json(results)

@app.route("/export/json/<path:ioc>")
def export_json_route(ioc):
    ioc_type = detect_ioc_type(ioc)
    analyzers = load_analyzers(ioc_type)
    results = {}
    for name, analyzer in analyzers.items():
        try:
            results[name] = analyzer.analyze(ioc)
        except Exception as e:
            results[name] = {"error": str(e)}
    return export_json(results)

@app.route("/export/pdf/<path:ioc>")
def export_pdf_route(ioc):
    ioc_type = detect_ioc_type(ioc)
    analyzers = load_analyzers(ioc_type)
    results = {}
    for name, analyzer in analyzers.items():
        try:
            results[name] = analyzer.analyze(ioc)
        except Exception as e:
            results[name] = {"error": str(e)}
    return export_pdf(ioc, results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
