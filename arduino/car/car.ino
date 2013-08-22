
#include <Servo.h> 
int incomingByte = 0;   // for incoming serial data
int a[4];
int motor = 3;

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


}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
           incomingByte = Serial.read();
           if (incomingByte == 48) {
            
            for (int p = 0; p < 4; p++){
                // read the incoming byte:
                while (Serial.available() <= 0) {
                delay(100);
                }
                a[p] = Serial.read();
                               
            }
            
            motor.write(a[0]); 
            steer.write(a[1]);
            camx.write(a[2]);
            camy.write(a[3]);
            
           }
        }

}

