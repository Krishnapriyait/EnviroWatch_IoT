from flask import Flask, render_template, jsonify
import threading
import time
import serial
import json
from pymongo import MongoClient

# === Arduino Serial Setup ===
SERIAL_PORT = 'COM5'   # ⚙️ Change this to your actual COM port (e.g., COM3 or /dev/ttyUSB0)
BAUD_RATE = 9600

# === MongoDB Setup ===
client = MongoClient("mongodb://localhost:27017/")
db = client["arduinoDB"]
collection = db["readings"]

# === Flask App ===
app = Flask(__name__)

# === Background function to read Arduino data and store in MongoDB ===
def read_from_arduino():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        ser.reset_input_buffer()
        print(f"✅ Connected to Arduino on {SERIAL_PORT}")

        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if line.startswith("{") and line.endswith("}"):
                try:
                    data = json.loads(line)

                    # Convert numeric sensor flags to readable text
                    if "flame" in data:
                        data["flame"] = "Detected" if int(data["flame"]) == 1 else "Normal"

                    # Ensure smoke key exists (if Arduino doesn’t send it)
                    if "smoke" not in data:
                        data["smoke"] = 0

                    # Add timestamp
                    data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

                    # Save to MongoDB
                    collection.insert_one(data)
                    print("💾 Saved to MongoDB:", data)

                except json.JSONDecodeError:
                    print("⚠️ Invalid JSON:", line)

    except serial.SerialException:
        print(f"❌ Could not open serial port {SERIAL_PORT}. Check your Arduino connection.")
    except Exception as e:
        print("❌ Error:", e)


# === Start background data reading thread ===
thread = threading.Thread(target=read_from_arduino, daemon=True)
thread.start()


# === Flask routes ===
@app.route("/")
def index():
    """Render the dashboard with the latest Arduino data."""
    latest = collection.find_one(sort=[("_id", -1)])
    return render_template("index.html", data=latest or {})


@app.route("/latest")
def latest_data():
    """Return the latest record as JSON (for frontend auto-update)."""
    latest = collection.find_one(sort=[("_id", -1)])
    if latest:
        latest["_id"] = str(latest["_id"])  # Convert ObjectId for JSON
    return jsonify(latest or {})


# === Main entry point ===
if __name__ == "__main__":
    print("🚀 Flask server running at http://127.0.0.1:5000/")
    app.run(debug=True)
