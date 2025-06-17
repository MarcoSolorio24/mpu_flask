import requests
import time
from sensor import read_sensor_data  # Usa tu sensor.py real

SERVER_URL = "http://3.15.139.1:5000/upload"

def send_data():
    while True:
        try:
            data = read_sensor_data()
            response = requests.post(SERVER_URL, json=data)
            print(f"Sent: {response.status_code} -> {response.text}")
        except Exception as e:
            print("Error:", e)
        time.sleep(1)

if __name__ == "__main__":
    send_data()
