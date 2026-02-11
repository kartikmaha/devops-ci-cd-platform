from flask import Flask, jsonify, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/info")
def info():
    return jsonify({
        "status": "UP",
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "build_number": os.getenv("BUILD_NUMBER", "local"),
        "git_commit": os.getenv("GIT_COMMIT", "unknown"),
        "deployed_at": datetime.utcnow().isoformat()
    })
    
@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
