#DISTANCE MEASUREMENT AND OBJECT DETECTION USING ULTRASONIC SENSORS WITH RASPBERRY PI PICO W

# Distance Measurement and Object Detection using Ultrasonic Sensors with Raspberry Pi Pico W

## 📌 Project Aim
To measure the distance and detect nearby objects using an **HC-SR04 ultrasonic sensor** interfaced with a **Raspberry Pi Pico W**, with visual alerts on an LCD and an LED.

---

## 🛠️ Hardware Required
- Raspberry Pi Pico W  
- Ultrasonic Sensor HC-SR04  
- 16x2 I2C LCD Display  
- Indicator LED  
- Buzzer (optional)  
- Jumper Wires  
- Breadboard  

---

## 🔌 Circuit Connections

| Component     | Pico W Pin |
|---------------|-----------|
| HC-SR04 VCC   | VBus      |
| HC-SR04 GND   | GND       |
| HC-SR04 ECHO  | GPIO16    |
| HC-SR04 TRIG  | GPIO17    |
| LCD SDA       | GPIO0     |
| LCD SCL       | GPIO1     |
| LED           | GPIO18    |

📂 [Circuit Diagram](circuit/circuit_diagram.png)

---

## 📊 Flowchart
The following flowchart explains the logic of the system:  
📂 [Flowchart](docs/flowchart.png)

---

## 💻 Code
Main program file is located in:  
📂 [code/ultrasonic_demo.py](code/ultrasonic_demo.py)
