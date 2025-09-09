# Embedded Fire Detection and Alarm Notification System (ESP32)

## 📌 Project Aim
To detect fire and notify the user by alarm using an **ESP32-S NodeMCU**, flame sensor, and DHT22 temperature sensor.

---

## 🛠️ Hardware Required
- ESP32-S NodeMCU  
- Flame Sensor (digital output)  
- DHT22 Sensor  
- LED  
- Buzzer  
- Jumper Wires  
- Arduino IDE  

---

## 🔌 Circuit Connections

| Component        | ESP32 Pin |
|------------------|-----------|
| Flame Sensor D0  | GPIO 27   |
| DHT22 Data Pin   | GPIO 4    |
| LED              | GPIO 26   |
| Buzzer           | GPIO 25   |
| VCC              | 5V        |
| GND              | GND       |

---

## 📊 Flowchart
📂 [Flowchart](docs/flame_sensor.png)

---

## 💻 Code
Main program file: **`code/flame_detection.py`**

```cpp
#include <DHT.h>

#define FLAME_DO_PIN  15   // Flame sensor digital output pin
#define DHT_PIN       14   // DHT11/22 data pin
#define BUZZER_PIN    18   // Buzzer pin
#define LED_PIN        2   // On-board LED

#define DHTTYPE DHT11
DHT dht(DHT_PIN, DHTTYPE);

const float TEMP_HIGH_C = 45.0;
const float TEMP_WARN_C = 30.0;

bool flameDetected = false;
float temperature = 0.0;
float humidity = 0.0;

void setup() {
  Serial.begin(115200);
  pinMode(FLAME_DO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  dht.begin();
  Serial.println("Fire Detection + Alarm System (ESP32)");
}

void loop() {
  flameDetected = (digitalRead(FLAME_DO_PIN) == LOW);
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("⚠ Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  bool alarm = false;
  String reason = "";

  if (flameDetected) {
    alarm = true;
    reason = "FLAME";
  } else if (temperature >= TEMP_HIGH_C) {
    alarm = true;
    reason = "TEMP HIGH";
  }

  if (alarm) {
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    delay(200);
    digitalWrite(BUZZER_PIN, LOW);
  } else {
    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
    delay(500);
  }

  Serial.print("Flame: ");
  Serial.print(flameDetected ? "DETECTED" : "No Flame");
  Serial.print(" | Temp: ");
  Serial.print(temperature);
  Serial.print(" C | Hum: ");
  Serial.print(humidity);
  Serial.print(" % | Alarm: ");
  Serial.println(alarm ? reason : "OFF");
}
