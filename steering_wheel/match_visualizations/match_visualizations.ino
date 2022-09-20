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
   if (message == "right\n"){ horiz_left(); vert_zero(); }
   else if (message=="left\n"){ horiz_right(); vert_zero(); }
   else if (message=="midleft\n"){ vert_zero(); servo1.write(95);}
   else if (message=="mid\n"){ horiz_zero(); vert_zero(); }
   else if (message=="midright\n"){ vert_zero(); servo1.write(40);}
   Serial.print(message);
 }
}

void horiz_zero(){ servo1.write(70); delay(300); }
void horiz_left(){ servo1.write(0);  delay(300); }
void horiz_right(){ servo1.write(120);  delay(300); }
void vert_zero(){ servo2.write(70);  delay(300); }
void vert_top(){ servo2.write(20);  delay(300); }
void vert_bot(){ servo2.write(120);  delay(300); }
