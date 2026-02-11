from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/metrics')
def metrics():
    # Simulated monitoring data
    data = {
        "ci_status": "Healthy",
        "build_success_rate": f"{random.randint(90, 100)}%",
        "active_pods": random.randint(2, 5),
        "cpu_usage": f"{random.randint(30, 70)}%",
        "memory_usage": f"{random.randint(40, 80)}%",
        "security_vulnerabilities": random.randint(0, 3)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
