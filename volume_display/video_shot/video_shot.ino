
#include <Servo.h>

Servo myservo; 

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(0);
}

void loop() {
  for(int pos=0; pos<50; pos+=2){
    myservo.write(pos);
    delay(50);
  }
  delay(1000);
  for(int pos=50; pos>0; pos-=2){
    myservo.write(pos);
    delay(50);
  }
  delay(1000);
  for(int pos=0; pos<50; pos+=2){
    myservo.write(pos);
    delay(50);
  }
  delay(500);
  for(int pos=50; pos>20; pos-=2){
    myservo.write(pos);
    delay(50);
  }
  delay(50);
  for(int pos=20; pos<50; pos+=2){
    myservo.write(pos);
    delay(50);
  }
  delay(500);
  for(int pos=50; pos>20; pos-=2){
    myservo.write(pos);
    delay(50);
  }
  delay(500);
  for(int pos=20; pos<50; pos+=2){
    myservo.write(pos);
    delay(50);
  }
  delay(500);    
  for(int pos=50; pos>0; pos-=2){
    myservo.write(pos);
    delay(50);
  }
  delay(3000);
}
