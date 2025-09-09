# 🌱 Automated Irrigation Control System using ESP8266

## 📌 Project Aim
To design and implement an automated irrigation control system that efficiently manages water delivery to crops by sensing **soil moisture, temperature, and humidity**, using the **ESP8266 microcontroller** for real-time monitoring, control, and remote management.  

---

## 🛠️ Hardware Required
- ESP8266 microcontroller  
- Soil Moisture Sensor  
- DHT22 Temperature & Humidity Sensor  
- Water Level Sensor (optional)  
- Motor Pump  
- Relay Module (2-channel)  
- Power Supply (3.3V/5V)  
- OLED Display (SSD1306)  
- LED Indicators  
- Connecting Wires & Breadboard  

---

## 🔌 Circuit Connections

| Pin Name | GPIO Number | Function |
|----------|-------------|----------|
| D0       | GPIO16      | Sensor input |
| D1       | GPIO5       | I2C SCL |
| D2       | GPIO4       | I2C SDA |
| A0       | ADC0        | Soil moisture sensor |
| D5       | GPIO14      | Relay control output |
| D6       | GPIO12      | Relay control output / sensor |
| D7       | GPIO13      | General purpose I/O (e.g., water level) |
| 3V3      | Power       | 3.3V supply |
| GND      | Power       | Ground reference |

📂 [Circuit Diagram](circuit/circuit_diagram.png)

---

## 📊 Flowchart
📂 [Flowchart](docs/flowchart.png)

---

## 💻 Code
Main program: **`code/irrigation_control.ino`**

```cpp
#define SOIL_PIN A0 
#define RELAY_PIN 5   
#define LED_PUMP 4    
#define LED_DRY 0     

int threshold = 600;  

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(LED_PUMP, OUTPUT);
  pinMode(LED_DRY, OUTPUT);

  // Relay OFF initially
  digitalWrite(RELAY_PIN, HIGH);
  digitalWrite(LED_PUMP, LOW);
  digitalWrite(LED_DRY, LOW);

  Serial.begin(9600);
  Serial.println("Automated Irrigation System Started");  
}

void loop() {
  int soilValue = analogRead(SOIL_PIN);
  Serial.print("Soil Moisture Value: ");
  Serial.println(soilValue);

  if (soilValue < threshold) {
    // Soil dry → Pump ON
    digitalWrite(RELAY_PIN, LOW);   // Active LOW relay
    digitalWrite(LED_PUMP, HIGH);
    digitalWrite(LED_DRY, HIGH);
    Serial.println("Soil Dry → Pump ON");
  } else {
    // Soil wet → Pump OFF
    digitalWrite(RELAY_PIN, HIGH);
    digitalWrite(LED_PUMP, LOW);
    digitalWrite(LED_DRY, LOW);
    Serial.println("Soil Wet → Pump OFF");
  }

  delay(1000);
}
