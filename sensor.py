import mpu6050
import time 

sensor = mpu6050.mpu6050(0x68)

def read_sensor_data():
    accelerometer_data = sensor.get_accel_data()
    gyroscope_data = sensor.get_gyro_data()
    temperature = sensor.get_temp()
    return {
        "accelerometer": accelerometer_data,
        "gyroscope": gyroscope_data,
        "temperature": temperature  # <-- corregido
    }

