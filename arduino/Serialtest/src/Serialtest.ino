int incomingByte = 0;   // for incoming serial data
int a[4];

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
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
                //Serial.print(a[p]);
                // say what you got                
            }
            Serial.print(a[0]);
            Serial.print(a[1]);
            Serial.print(a[2]);
            Serial.print(a[3]);
            Serial.println();
            //for (int i = 0; i < 4; i++) {
            //Serial.print(a[i]);
            //Serial.print(",");
            //}
           }
        }
}
