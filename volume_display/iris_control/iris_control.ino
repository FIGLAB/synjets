/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo; 

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(0);
}

void loop() {
  while (Serial.available() > 0)
 {
   String message = Serial.readString();
   if (message=="open"){
    myservo.write(0);
    delay(50);
   } else if (message=="close"){
    myservo.write(40);
    delay(50);
   } else if (message=="mopen"){
    myservo.write(40);
    delay(50);
    for(int pos=40; pos>0; pos-=2){
      myservo.write(pos);
      delay(50);
    }
   } else if (message=="mclose"){
    myservo.write(0);
    delay(50);
    for(int pos=0; pos<40; pos+=2){
      myservo.write(pos);
      delay(50);
    }
   } 
   else if (message=="moc"){
    myservo.write(0);
    delay(50);
    for(int pos=0; pos<40; pos+=2){
      myservo.write(pos);
      delay(30);
    }
    for(int pos=40; pos>0; pos-=2){
      myservo.write(pos);
      delay(30);
    }
    for(int pos=0; pos<40; pos+=2){
      myservo.write(pos);
      delay(30);
    }
    for(int pos=40; pos>0; pos-=2){
      myservo.write(pos);
      delay(30);
    }
    
   }
 }
}
