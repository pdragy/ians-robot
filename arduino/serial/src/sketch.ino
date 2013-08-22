
int led = 13;
void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);     
    int num;
}

void loop()
{
   if (Serial.available() > 0) {
    blink(Serial.read() - '0');
    delay(1000);
   }
}

void blink(int n) {
    int i;
    for (i = 0; i < n; i++) {
      digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(200);               // wait for a second
      digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
      delay(200);               // wait for a second
    }
}

