//declare pins LED is attached to
const int angryPin = 5;
const int sadPin = 4;
const int happyPin = 3;
const int neutralPin = 2;
const int buzzer = 13;

int incomingByte;  // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pins as an output:
  pinMode(angryPin, OUTPUT);
  pinMode(sadPin, OUTPUT);
  pinMode(happyPin, OUTPUT);
  pinMode(neutralPin, OUTPUT);
  pinMode(buzzer, OUTPUT);
}


void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();

    if (incomingByte == 'A') {
      digitalWrite(angryPin, HIGH);
      digitalWrite(sadPin, LOW);
      digitalWrite(happyPin, LOW);
      digitalWrite(neutralPin, LOW);
      digitalWrite(buzzer, HIGH);
    }

    if (incomingByte == 'S') {
      digitalWrite(angryPin, LOW);
      digitalWrite(sadPin, HIGH);
      digitalWrite(happyPin, LOW);
      digitalWrite(neutralPin, LOW);
      digitalWrite(buzzer, LOW);
    }

    if (incomingByte == 'H') {
      digitalWrite(angryPin, LOW);
      digitalWrite(sadPin, LOW);
      digitalWrite(happyPin, HIGH);
      digitalWrite(neutralPin, LOW);
      digitalWrite(buzzer, LOW);
    }

    if (incomingByte == 'N') {
      digitalWrite(angryPin, LOW);
      digitalWrite(sadPin, LOW);
      digitalWrite(happyPin, LOW);
      digitalWrite(neutralPin, HIGH);
      digitalWrite(buzzer, LOW);
    }
  }
}
