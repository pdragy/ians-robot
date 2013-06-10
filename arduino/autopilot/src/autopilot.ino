// last modified 10/28/12
// 

#include <Servo.h> 
#define trigPin 12
#define echoPin 11
#define locations 3
#define forward 5
#define reverse 3
#define left 9
#define right 10
#define servo_pin 6

// globals 
int j[10];
int Ave, val;
Servo myservo;  // create servo object to control a servo 
 
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(forward, OUTPUT);
  pinMode(reverse, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);
  pinMode(echoPin, INPUT);
  myservo.attach(servo_pin);  
  digitalWrite(trigPin, HIGH);
}

void loop() {
   cruise();
   // if (distance< 20){
   check();
   delay(100);
   if (Ave < 40 && Ave > 2){
     turn(); 
   }
}

int cruise() {
  int duration, distance;
  while(1){
    for(int x=0; x< locations*2; x++){
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(1000);
      digitalWrite(trigPin, LOW);
      duration = pulseIn(echoPin, HIGH, 6000);
      distance = (duration/2) / 29.1;
      if (distance >= 100 || distance <= 0){
        Serial.println("Out of range");
        distance = 100;
      } else {
        Serial.print(distance);
        Serial.println(" cm");
      }
      if( distance < 40 && distance> 2){
         return (distance) ;
      }
      val =sqrt(sq(179-(x*((179*2)/(locations*2))))); 
      myservo.write(val); // sets the servo position according to the scaled value 
      delay(200);
      analogWrite(forward, 110);
      analogWrite(reverse, 0);
      digitalWrite(left, LOW);
      digitalWrite(right, LOW);
     } // end for
  } // end while
}

int check(){
  int dur, dis, tot;
  for(int i=0; i< 10 ; i++){
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(trigPin, LOW);
    dur = pulseIn(echoPin, HIGH, 6000);
    dis = (dur/2) / 29.1;
    if (dis >= 100 || dis <= 0) {
      Serial.println("Out of range check");
      dis= 100;
    } else {
      Serial.print(dis);
      Serial.println(" cm check");
    }
    j[i]=dis;
  }
  tot = 0;
  for(int k = 0 ; k < 10; k++) {
    tot = tot + j[k];
  }
  Ave = tot/10;
  return (Ave);
}

void turn() {
  analogWrite(reverse, 100);
  analogWrite(forward, 0);
  digitalWrite(right, LOW);
  digitalWrite(left, LOW);
  delay(2000);
  analogWrite(reverse, 0);
  analogWrite(forward, 0);
  delay(500);
  if(val < 95){
    digitalWrite(right, HIGH);
    digitalWrite(left, LOW);
  }
  else{
    digitalWrite(left, HIGH);
    digitalWrite(right, LOW);
  }
  analogWrite(forward, 100);
  analogWrite(reverse, 0);
  delay(2000);
}
  
