from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Mock API for status updates
@app.route('/api/status')
def get_status():
    return jsonify({
        "status": "Success",
        "last_run": "2 mins ago",
        "commit": "a7b2c3d"
    })

if __name__ == '__main__':
    app.run(debug=True)
