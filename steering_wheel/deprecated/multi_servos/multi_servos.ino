#include <Servo.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;
const unsigned int MAX_MESSAGE_LENGTH = 12;
static char message[MAX_MESSAGE_LENGTH];
static unsigned int message_pos = 0;
int curr_up = 70;
int curr_left = 70;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  Serial.setTimeout(1);
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

   int number = message.toInt();
   if (number < 121 && number >= 0){
    if(number > curr_left){      
      for (int a = curr_left; a < number; a += 5){
        servo1.write(a);
        delay(50);
      }
    }
    else{      
      for (int a = curr_left; a > number; a -= 5){
        servo1.write(a);
        delay(50);
      }
    }
    servo1.write(number);
    curr_left = number;
   }
   else if (number < 611 && number >= 500){
    servo1.write(number - 500);
    delay(50);
   }
   else if (number < 321 && number >= 200) {
    number -= 200;
    if(number > curr_up){      
      for (int a = curr_up; a < number; a += 5){
        servo2.write(a);
        delay(50);
      }
    }
    else{      
      for (int a = curr_up; a > number; a -= 5){
        servo2.write(a);
        delay(50);
      }
    }
    servo2.write(number);
    curr_up = number;
   }
   else if (number < 816 && number >= 700){
    servo2.write(number - 700);
    delay(50);
   }
   Serial.println(number);
 }
}
