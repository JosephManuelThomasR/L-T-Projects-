# 💧 Real-Time Water Quality Monitoring and Analysis System (ESP8266 + Turbidity Sensor)

## 📌 Project Aim
To design and develop a **real-time water quality monitoring system** using a **turbidity sensor** interfaced with an **ESP8266 microcontroller**. The system continuously measures turbidity, processes the data, and displays results in **Nephelometric Turbidity Units (NTU)** on an I2C OLED screen for immediate water clarity assessment.  

---

## 🛠️ Hardware Required
- ESP8266 (NodeMCU) Microcontroller  
- Water Turbidity Sensor Module  
- I2C OLED Display Module (0.96", 128x64)  
- Breadboard  
- Jumper Wires  
- 5V Power Supply  

---

## 🔌 Circuit Connections

| Component Pin            | ESP8266 (NodeMCU) Pin |
|--------------------------|------------------------|
| Turbidity Sensor VCC     | 5V (Vin)              |
| Turbidity Sensor GND     | GND                   |
| Turbidity Sensor AOUT    | A0                    |
| OLED Display VCC         | 3.3V                  |
| OLED Display GND         | GND                   |
| OLED Display SDA         | D2 (GPIO4)            |
| OLED Display SCL         | D1 (GPIO5)            |

📂 [Circuit Diagram](circuit/circuit_diagram.png)

---

## 📊 Flowchart
📂 [water Monitoring System Workflow](water_system_flow.png)

---

## 💻 Code
Main program: **`code/water_quality_monitor.ino`**

```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 64 
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

int turbidityPin = A0;  
#define OLED_SDA 4
#define OLED_SCL 5   

void setup() {
  Serial.begin(115200);
  Wire.begin(OLED_SDA, OLED_SCL);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Loop forever if display fails
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(10, 10);
  display.println("Water Quality");
  display.println("  Monitor");
  display.display();
  delay(2000);
}

void loop() {
  int turbidityValue = analogRead(turbidityPin);
  float voltage = turbidityValue * (3.3 / 1023.0);
  float turbidityNTU = -1120.4 * square(voltage) + 5742.3 * voltage - 4352.9;

  if (turbidityNTU < 0) turbidityNTU = 0;

  Serial.print("Raw Value: "); 
  Serial.print(turbidityValue);
  Serial.print(" | Voltage: "); 
  Serial.print(voltage);
  Serial.print("V | Turbidity: "); 
  Serial.print(turbidityNTU, 2); 
  Serial.println(" NTU");

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.println("Water Quality Monitor");
  display.drawLine(0, 10, 127, 10, WHITE); 
  display.setTextSize(2);
  display.setCursor(0, 25);
  display.print("Turb:");
  display.setCursor(60, 25);
  display.print(turbidityNTU, 1); 
  display.println(" NTU");
  display.display();

  delay(1000); 
}
