from flask import Flask, jsonify, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/info")
def info():
    return jsonify({
        "application": "CI/CD Pipeline Showcase Dashboard",
        "status": "UP",
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "build_number": os.getenv("BUILD_NUMBER", "manual"),
        "git_commit": os.getenv("GIT_COMMIT", "local"),
        "deployed_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    })

@app.route("/api/tools")
def tools():
    return jsonify({
        "tools": [
            {"name": "GitHub", "purpose": "Source Code Management"},
            {"name": "Jenkins", "purpose": "CI/CD Automation"},
            {"name": "Docker", "purpose": "Containerization"},
            {"name": "Ansible", "purpose": "Configuration Management & Deployment"},
            {"name": "AWS EC2", "purpose": "Application Hosting"}
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
