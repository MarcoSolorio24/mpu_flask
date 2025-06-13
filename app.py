from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

# Variable global para almacenar los últimos datos recibidos
sensor_data = {
    "accelerometer": {"x": 0, "y": 0, "z": 0},
    "gyroscope": {"x": 0, "y": 0, "z": 0},
    "temperature": 0,
    "timestamp": time.time()
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sensor_data)

@app.route('/upload', methods=['POST'])
def upload_data():
    global sensor_data
    if request.is_json:
        data = request.get_json()
        data["timestamp"] = time.time()
        sensor_data = data
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"error": "Invalid JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
