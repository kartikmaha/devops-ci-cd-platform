from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

def app_metadata():
    return {
        "status": "UP",
        "service": "devops-ci-cd-platform",
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "git_commit": os.getenv("GIT_COMMIT", "unknown"),
        "build_number": os.getenv("BUILD_NUMBER", "unknown"),
        "deployed_at": os.getenv("DEPLOY_TIME", datetime.utcnow().isoformat())
    }

@app.route("/")
def home():
    return jsonify(app_metadata())

@app.route("/info")
def info():
    return jsonify(app_metadata())

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
