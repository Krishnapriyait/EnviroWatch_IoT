import serial
import time
import json

SERIAL_PORT = 'COM5'   # change to your Arduino COM port
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # wait for Arduino to reset
    ser.reset_input_buffer()  # clear old messages

    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line.startswith("{") and line.endswith("}"):  # only JSON
            try:
                data = json.loads(line)
                data["flame"] = "Detected" if data["flame"] == 1 else "Normal"
                print(data)
            except json.JSONDecodeError:
                print("JSON decode error:", line)
        else:
            print("Ignored line:", line)

except Exception as e:
    print("Error:", e)
