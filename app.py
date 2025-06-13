from flask import Flask, render_template, jsonify
from sensor import read_sensor_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(read_sensor_data())

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port = 5000, debug = True)


