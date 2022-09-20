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
   //Read the next available byte in the serial receive buffer
   String message = Serial.readString();
   
   //Print the message (or do other things)
   if (message == "o\n" || message == "o"){ 
      myservo.write(0);
   }
   if (message == "c\n" || message == "c"){ 
      myservo.write(50);
   }
   Serial.print(message);
 }
}
