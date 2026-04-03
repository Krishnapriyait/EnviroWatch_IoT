# AeroFire Shield

**IoT-based Environmental Monitoring and Fire Detection System**

---

## Project Description

**AeroFire Shield** is an IoT-based smart environmental monitoring and fire detection system designed to improve safety through real-time monitoring and instant alerts. The system continuously tracks temperature, humidity, air quality, smoke level, and flame presence using sensors connected to an Arduino microcontroller.

The sensor data is transmitted to a Python Flask web application, where it is processed and displayed on a live dashboard. Users can monitor environmental conditions in real time from any device using a web interface.

The system also sends instant alert notifications to the admin when abnormal conditions such as fire risk, high smoke levels, or unsafe air quality are detected. This helps ensure quick response and prevents potential hazards.

For advanced monitoring and analysis, the project integrates with ThingSpeak, which stores sensor data in the cloud and provides data visualization, graphs, and analytics. This enables tracking of environmental patterns and early detection of risks.

The system is designed to be low-cost, efficient, and easy to implement, making it suitable for homes, industries, laboratories, and public places.

---

## Objectives

* Monitor environmental parameters in real time
* Detect fire hazards early using sensors
* Provide instant alert notifications to admin
* Display live data through web dashboard
* Store sensor data in cloud for analytics
* Improve safety using IoT technology

---

## Key Features

* Real-time environmental monitoring
* Detects temperature, humidity, smoke, air quality, and flame
* Live dashboard using Flask web application
* Admin notification alert during abnormal conditions
* Cloud storage and analytics using ThingSpeak
* Buzzer and LED alert system
* Low-cost IoT safety solution

---

## Technologies Used

### Hardware

* Arduino Uno
* DHT11 Sensor (Temperature & Humidity)
* MQ2 Sensor (Smoke Detection)
* Flame Sensor
* Buzzer
* LED

### Software

* Arduino IDE
* Python
* Flask Framework
* HTML
* CSS
* JavaScript
* PySerial Library
* ThingSpeak

---

## System Architecture

Sensors collect environmental data → Arduino processes data → Python Flask server reads serial data → Web dashboard displays live values → Admin receives alert notification → Data stored in ThingSpeak cloud for analytics.

---

## Output

* Live sensor readings displayed in web dashboard
* Graph visualization in ThingSpeak
* Alert notification sent to admin
* Buzzer sound and LED indication during risk condition

---

## Project Structure

```
AeroFire-Shield/
│
├── arduino/
│   └── sensor_code.ino
│
├── python/
│   └── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── docs/
│   ├── report.pdf
│   └── presentation.pptx
│
├── demo/
│   └── demo_video.mp4
│
└── README.md
```

---

## How to Run the Project

### Step 1: Upload Arduino Code

* Connect Arduino Uno
* Open Arduino IDE
* Upload sensor code to Arduino

### Step 2: Run Python Server

Install required libraries:

```
pip install flask pyserial
```

Run the program:

```
python app.py
```

### Step 3: Open Web Dashboard

Open browser and go to:

```
http://127.0.0.1:5000
```

---

## Screenshots



---

## 🎥 Demo Video

Demo video is present inside the demo folder

---

## ThingSpeak Analytics

Sensor data is stored in ThingSpeak cloud and visualized using graphs for analysis.

---

## License

This project is for educational purposes.
