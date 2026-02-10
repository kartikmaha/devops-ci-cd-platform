from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import datetime
import os

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests received"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Application is running"

@app.route("/info")
def info():
    REQUEST_COUNT.inc()
    return jsonify({
        "environment": os.getenv("ENV", "production"),
        "build": os.getenv("BUILD_NUMBER", "manual-build"),
        "time": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    })

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
