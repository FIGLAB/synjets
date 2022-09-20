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
  vert_zero();
  horiz_right();
  for(int pos = 20; pos < 120; pos += 5){   // LEFT SWIPE
    servo1.write(pos);
    delay(50);
  }
  delay(2000);
  for(int pos = 115; pos > 20; pos -= 5){   // RIGHT SWIPE
    servo1.write(pos);
    delay(50);
  }
  delay(2000);
  horiz_zero();
  vert_bot();
  delay(2000);                              // TOP
  for(int pos = 115; pos > 0; pos -= 5){   // DOWN SWIPE
    servo2.write(pos);
    delay(50);
  }
  delay(2000);
  for(int pos = 0; pos < 120; pos += 5){   // UP SWIPE
    servo2.write(pos);
    delay(50);
  }
  delay(2000);
}

void horiz_zero(){ servo1.write(70); delay(300); }
void horiz_left(){ servo1.write(20);  delay(300); }
void horiz_right(){ servo1.write(120);  delay(300); }
void vert_zero(){ servo2.write(70);  delay(300); }
void vert_top(){ servo2.write(20);  delay(300); }
void vert_bot(){ servo2.write(120);  delay(300); }
