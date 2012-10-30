#define motoron 2
#define forward 5
#define reverse 3
#define left 9
#define right 10
#define steeron 8
#define steerin 4
#define speedin 7

int d=0;
int Y=0;
int fwd= 0;
int rev= 0;
int rght= 0;
int lft= 0;

int main() {}

void setup() {                
    pinMode(steerin, INPUT);         // set receiver pins
    pinMode(speedin, INPUT);
    Serial.begin (9600); 
    digitalWrite(motoron, HIGH);     // set power pins on
    digitalWrite(steeron, HIGH);
}

void loop() {
  d=pulseIn(speedin, HIGH);       //receiver drive output
  //Serial.print(d);
  //Serial.println();
  fwd= map(d, 1600, 950, 0, 255);
  rev= map(d, 1600, 2100, 0, 255);
  
  if(d <1525 && d> 100){                  //go forward
    analogWrite(forward, fwd);
    analogWrite(reverse, 0);
  }
  else if(d >= 1525 && d<= 1675){        //if at nuetral keep motors off
    
   analogWrite(forward, 0);
   analogWrite(reverse, 0);
  }
  else if (d >1675 && d < 2100){          //go reverse
    analogWrite(reverse, rev);
    analogWrite(forward, 0);
  }
  else if (d<=100 && d >= 2100){          //shut motors off if odd data or remote is off
     analogWrite(forward, 0);
   analogWrite(reverse, 0);
  }
  //Serial.print(d);
  //Serial.println();
  //steering
    Y=pulseIn(steerin, HIGH);            // receiver data
  //Serial.print(Y);
  //Serial.println();
  rght= map(Y, 1500, 2050, 0, 255);
  lft= map(Y, 1500, 1000, 0, 255);
  if(Y <1425 && Y> 100){                // go left
    analogWrite(left, lft);
    analogWrite(right, 0);
  }
  else if(Y >= 1425 && Y<= 1600){        // at neutral position shut motor off
   analogWrite(right, 0);
   analogWrite(left, 0);
  }
  else if (Y >1600 && Y < 2100){          // turn right
    analogWrite(right, rght);
    analogWrite(left, 0);
  }
  else if (Y<=100 &&  Y >= 2100){        // shut motors off when remote is off
     analogWrite(right, 0);
   analogWrite(left, 0);
  }
  Serial.print(lft);
  Serial.println();
}
