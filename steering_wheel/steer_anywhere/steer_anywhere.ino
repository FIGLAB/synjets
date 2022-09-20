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
   int s1_pos = Serial.parseInt();
   int s2_pos = Serial.parseInt();
//   servo1.write(s1_pos);
   delay(100);
//   servo2.write(s2_pos);
   delay(100);
   Serial.print(s1_pos);
   Serial.println(s2_pos);
 }
}
