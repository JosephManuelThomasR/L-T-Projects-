# Motion and Position Tracking System using ESP32 & MPU6050

## 📌 Project Aim
To design and implement a system capable of detecting and analyzing **real-time orientation, acceleration, and angular velocity** using the **MPU6050 sensor**, with data displayed on an **OLED display** and motion alerts triggered via a buzzer.  

---

## 🛠️ Hardware Required
- ESP32 Dev Board  
- MPU6050 Sensor Module  
- SSD1306 OLED Display (128x64)  
- TMB12A05 Buzzer  
- Jumper Wires  
- Breadboard  
- Power Source (USB or battery)  

---

## 🔌 Circuit Connections

| ESP32 Pin | MPU6050 Pin | OLED Display Pin | Buzzer |
|-----------|-------------|------------------|--------|
| 3.3V      | VCC         | VCC              | -      |
| GND       | GND         | GND              | -      |
| GPIO21    | SDA         | SDA              | -      |
| GPIO22    | SCL         | SCL              | -      |
| GPIO25    | -           | -                | +      |
| GND       | -           | -                | -      |

📂 [Circuit Diagram](circuit/motion_circuit.png)

---

## 📊 Flowchart
📂 [Motion and Position Tracking Workflow](docs/motion_workflow.png)

---

## 💻 Code
Main program: **`code/motion_tracking.ino`**

```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_MPU6050.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define BUZZER 25

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
Adafruit_MPU6050 mpu;

float offX=0, offY=0, offZ=0;

void calibrateMPU(int n=500){
  Serial.println("Calibrating... Keep MPU6050 still!");
  for(int i=0;i<n;i++){
    sensors_event_t a,g,t; mpu.getEvent(&a,&g,&t);
    offX+=a.acceleration.x; offY+=a.acceleration.y; offZ+=a.acceleration.z-9.81;
    delay(5);
  }
  offX/=n; offY/=n; offZ/=n;
  Serial.printf("Offsets: %.2f, %.2f, %.2f\n", offX, offY, offZ);
}

void setup(){
  Serial.begin(115200);
  pinMode(BUZZER,OUTPUT); digitalWrite(BUZZER,LOW);

  if(!display.begin(SSD1306_SWITCHCAPVCC,0x3C)){
    Serial.println("SSD1306 fail"); for(;;);
  }
  display.clearDisplay(); display.setTextSize(1); display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0); display.println("MPU6050 Init..."); display.display();

  if(!mpu.begin()){Serial.println("MPU6050 fail"); while(1) delay(10);}
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(1000); calibrateMPU();
  display.clearDisplay(); display.setCursor(0,0); display.println("Calibration Done!");
  display.display(); delay(1000);
}

void loop(){
  sensors_event_t a,g,t; mpu.getEvent(&a,&g,&t);

  float x=a.acceleration.x-offX, y=a.acceleration.y-offY, z=a.acceleration.z-offZ;

  display.clearDisplay(); display.setCursor(0,0); display.setTextSize(1);
  display.printf("Acc X: %.2f\nAcc Y: %.2f\nAcc Z: %.2f\n", x, y, z);

  bool motion=false;
  if(fabs(x)>4){display.setTextSize(2); display.println("X Motion!"); Serial.println("⚠ Motion on X axis!"); motion=true;}
  if(fabs(y)>4){display.setTextSize(2); display.println("Y Motion!"); Serial.println("⚠ Motion on Y axis!"); motion=true;}
  if(fabs(z)>10){display.setTextSize(2); display.println("Z Motion!"); Serial.println("⚠ Motion on Z axis!"); motion=true;}

  display.display();
  digitalWrite(BUZZER,motion?HIGH:LOW);
  delay(100);
}
