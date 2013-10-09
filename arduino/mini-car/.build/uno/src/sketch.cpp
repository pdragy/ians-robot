#include <Arduino.h>
void setup();
void loop();
#line 1 "src/sketch.ino"

#include <Servo.h> 

int incomingByte = 0;   // for incoming serial data
int a[4];
int md1 = 3;
int md2=4;
int mp=5;
int sd1=8;
int sd2=9;
int sp=10;
int sm = 0;
int st = 0;
int sf=0;
int se=0;
void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        pinMode(md1, OUTPUT);
        pinMode(md2, OUTPUT);
        pinMode(mp, OUTPUT);
        pinMode(sd1, OUTPUT);
        pinMode(sd2, OUTPUT);
        pinMode(sp, OUTPUT);
}

void loop() {
        // send data only when you receive data:
        if (Serial.available() > 0) {
           //Serial.println("Serial available");
           incomingByte = Serial.read();
           if (incomingByte == 48) {
               //Serial.println("Serial = 48");
                for (int p = 0; p < 4; p++){
                    // read the incoming byte:
                    while (Serial.available() <= 0) {
                        delay(10);
                    }
                    a[p] = int(Serial.read());
                }
                //Serial.println(a[0]); 
                //Serial.println(a[1]);
                sm = 0;
                st = 0;
                sf=0;
		se=0;
                if (a[0] > 140){
                    sm = map(a[0], 140, 255, 0, 255);
                    digitalWrite(md1, HIGH);
                    digitalWrite(md2, LOW);
                    analogWrite(mp, sm);
                }

                if ((110 <= a[0]) && (a[0] <= 140)){
                    //sm= map(a[0], 95, 255, 0, 255);
                    digitalWrite(md1, LOW);
                    digitalWrite(md2, LOW);
                    analogWrite(mp, 0);
                }
                if (  a[0] <  110){
                    sf= map(a[0], 110, 0, 0, 255);
                    digitalWrite(md1, LOW);
                    digitalWrite(md2, HIGH);
                    analogWrite(mp, sf);
                }



		if (a[1] > 140){
                    st = map(a[1], 140, 255, 0, 255);
                    digitalWrite(sd1, HIGH);
                    digitalWrite(sd2, LOW);
                    analogWrite(sp, st);
                }

                if ((110 <= a[1]) && (a[1] <= 140)){
                    //sm= map(a[1], 95, 255, 0, 255);
                    digitalWrite(sd1, LOW);
                    digitalWrite(sd2, LOW);
                    analogWrite(sp, 0);
                }
                if (  a[1] <  110){
                    se= map(a[1], 110, 0, 0, 255);
                    digitalWrite(sd1, LOW);
                    digitalWrite(sd2, HIGH);
                    analogWrite(sp, se);
                }
               //Serial.print("sf");
               //Serial.print(sf);
               //Serial.print(", sm");
               //Serial.println(sm);

          }
    }
    delay(5);
}


