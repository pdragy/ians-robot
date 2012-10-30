#define trigPin 12
#define echoPin 11
#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
unsigned long time;
unsigned long last_time;
int val;
int i;
int turn;
unsigned long turn_threshold;
unsigned long sensor_threshold;
int turn_amount, duration, distance;
int distances[150*2];
int distance_cutoff;
int turn_step;
int smallest_distance;
int d_index;

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
   myservo.attach(6);  
  digitalWrite(12, HIGH);
  time = millis();
  last_time = time;
  turn_amount = -100;
  distance_cutoff = 100;
  turn_step = 10;
  smallest_distance = 100000;
  for (i = -turn_amount; i <= turn_amount; i = i + turn_step) {
    distances[i] = 0;
  }
}

void loop() {
    time = millis();
    //myservo.write(90);
    if ((time-last_time) >= 100) {
      last_time = time;
      turn_amount = turn_amount + turn_step;
      if (turn_amount >= 150 ) {
        turn_amount = -turn_amount;
      }
      
      val = abs(turn_amount);
      myservo.write(val);
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(2000);
      digitalWrite(trigPin, LOW);
      duration = pulseIn(echoPin, HIGH);
      distance = (duration/2) / 29.1;

      if (distance >= distance_cutoff || distance <= 0){
        //Serial.println("Out of range");
        Serial.println("-1");
        distance = -1;
      }
      else {
        Serial.println(distance);
        //Serial.println(" cm");
      }
      if (distances[val] <= 0) {
        if (distance < smallest_distance) {
          smallest_distance = distance;
          d_index = val;
        }
        distances[turn_amount] = distance;
      } else {
        if (distance < smallest_distance) {
           Serial.println(" distance");
           val = abs(turn_amount);
           myservo.write(d_index);
           delayMicroseconds(100);
          while (((distance -5) <= smallest_distance) &&(smallest_distance <= (distance+5))) {
            digitalWrite(trigPin, HIGH);
            delayMicroseconds(2000);
            digitalWrite(trigPin, LOW);
            duration = pulseIn(echoPin, HIGH);
            distance = (duration/2) / 29.1;
            delayMicroseconds(1000);
          }
          for (i = -turn_amount; i <= turn_amount; i = i + turn_step) {
            distances[i] = 0;
          }
          smallest_distance = 100000;
        }
      }  
        
    }   
}   

