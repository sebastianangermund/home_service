int analogPin = A0;
int LED = 13;
int val = 0;
int tempVal = 0;

String thing_id = "b909b44d-8772-419b-9b60-f2771c748a32";

void setup() {
  Serial.begin(115200);
}

// the loop function runs over and over again forever
void loop() {
  val = analogRead(analogPin);
  if (val > tempVal + 50) {
    digitalWrite(LED, HIGH);
    tempVal = val;
  }
  if (val < tempVal - 50) {
    digitalWrite(LED, LOW);
    tempVal = val;
  }
  delay(1000);
}
