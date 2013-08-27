
#include <Servo.h> 
int incomingByte = 0;   // for incoming serial data
int a[4];
//int go = 3;

Servo motor;
Servo steer;
Servo camx;
Servo camy;

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        motor.attach(3);
        steer.attach(5);
        camx.attach(6);
        camy.attach(9);
        a[0] = 89;
        a[1] = 89;
        motor.write(a[0]); 
        steer.write(a[1]);
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
           incomingByte = Serial.read();
           if (incomingByte == 48) {
               Serial.println("Got a 0");
            
            for (int p = 0; p < 4; p++){
                // read the incoming byte:
                int t=0;
                while (Serial.available() <= 0) {
                    //t++;
                  delay(100);
                  //if (t>5){
                  // motor.write(89);
                  //steer.write(89); 
                  //Serial.println("89 89"); 
                  //}
                }
                //Serial.println("reading a number");
                a[p] = Serial.read();
                               
            }
            
            motor.write(a[0]); 
            steer.write(a[1]);
            //camx.write(a[2]);
            //camy.write(a[3]);
            Serial.print(a[0]);
            Serial.print(" ");
            Serial.println(a[1]);
            
           }
        }
}
