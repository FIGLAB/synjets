#include <Servo.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);
  servo1.attach(5);
  servo2.attach(6); 
  servo1.write(70);
  servo2.write(70);
}

void loop() {
  while (Serial.available() > 0)
 {
   //Read the next available byte in the serial receive buffer
   String message = Serial.readString();
   
   //Print the message (or do other things)
   if (message=="ls"){
      for(int pos = 20; pos < 120; pos += 5){
        servo1.write(pos);
        delay(50);
      }
   } else if (message=="rs"){
      for(int pos = 115; pos > 20; pos -= 5){
        servo1.write(pos);
        delay(50);
      }
   } else if (message=="ds"){
      for(int pos = 115; pos > 20; pos -= 5){
        servo2.write(pos);
        delay(50);
      }
   } else if (message=="us"){
      for(int pos = 20; pos < 120; pos += 5){
        servo2.write(pos);
        delay(50);
      }
   } else if (message=="circle"){
      servo1.write(70);
      servo2.write(20);
      delay(300);
      servo1.write(120);
      servo2.write(70);
      delay(300);
      servo1.write(70);
      servo2.write(120);
      delay(300);
      servo1.write(20);
      servo2.write(70);
      delay(300);
   }
   else if (message == "right"){ horiz_left(); vert_zero(); }
   else if (message=="left"){ horiz_right(); vert_zero(); }
   else if (message=="bot"){ horiz_zero(); vert_top(); }
   else if (message=="midbot"){ horiz_zero(); servo2.write(45);}
   else if (message=="mid"){ horiz_zero(); vert_zero(); }
   else if (message=="midtop"){ horiz_zero(); servo2.write(95);}
   else if (message=="top"){ horiz_zero(); vert_bot(); }

   Serial.print(message);
 }
}

void horiz_zero(){ servo1.write(70); delay(300); }
void horiz_left(){ servo1.write(20);  delay(300); }
void horiz_right(){ servo1.write(120);  delay(300); }
void vert_zero(){ servo2.write(70);  delay(300); }
void vert_top(){ servo2.write(20);  delay(300); }
void vert_bot(){ servo2.write(120);  delay(300); }
