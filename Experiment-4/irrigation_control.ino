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
    digitalWrite(RELAY_PIN, LOW);   // Relay active (active LOW module)
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
