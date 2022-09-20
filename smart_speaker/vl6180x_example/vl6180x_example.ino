#include <SF1eFilter.h>
#include <Wire.h>
#include "Adafruit_VL6180X.h"

Adafruit_VL6180X vl = Adafruit_VL6180X();
int led = 13;
int outpin = 22;
int stat = 0;
int aRes = 12;
double range = 1.0;
double filtered = 0.0;
float fs = 100;
float minCutoffFrequency = 2;
float cutoffSlope = .02;
float derivativeCutoffFrequency = 50;
SF1eFilter *filter;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  analogWriteResolution(aRes);
  // wait for serial port to open on native usb devices
  //while (!Serial) {
  //  delay(1);
  //}
  filter = SF1eFilterCreate(fs, minCutoffFrequency, cutoffSlope, derivativeCutoffFrequency);
  SF1eFilterInit(filter);
  Serial.println("Adafruit VL6180x test!");
  if (! vl.begin()) {
    Serial.println("Failed to find sensor");
    while (1);
  }
  Serial.println("Sensor found!");
}

void loop() {
  // float lux = vl.readLux(VL6180X_ALS_GAIN_5);

  // Serial.print("Lux: "); Serial.println(lux);
  range = vl.readRange();
  double timestamp = millis()/1000.0;
  filtered = SF1eFilterDoAtTime(filter, range, timestamp);
  uint8_t status = vl.readRangeStatus();

  if (status == VL6180X_ERROR_NONE) {
//    Serial.print(range);
//    Serial.print(',');
    Serial.println(filtered);
    analogWrite(outpin, filtered/200.0*pow(2,aRes));
    
    if(stat==0){
      digitalWrite(led, HIGH);
      stat = 1;
    }
    else {
      digitalWrite(led, LOW);
      stat = 0;
    } 
    
  } else {
    analogWrite(outpin, 0);
  Serial.println(300);
  }

  // Some error occurred, print it out!
  
//  if  ((status >= VL6180X_ERROR_SYSERR_1) && (status <= VL6180X_ERROR_SYSERR_5)) {
//    Serial.println("ERROR: System error");
//  }
//  else if (status == VL6180X_ERROR_ECEFAIL) {
//    Serial.println("ERROR: ECE failure");
//  }
//  else if (status == VL6180X_ERROR_NOCONVERGE) {
//    Serial.println("ERROR: No convergence");
//  }
//  else if (status == VL6180X_ERROR_RANGEIGNORE) {
//    Serial.println("ERROR: Ignoring range");
//  }
//  else if (status == VL6180X_ERROR_SNR) {
//    Serial.println("ERROR: Signal/Noise error");
//  }
//  else if (status == VL6180X_ERROR_RAWUFLOW) {
//    Serial.println("ERROR: Raw reading underflow");
//  }
//  else if (status == VL6180X_ERROR_RAWOFLOW) {
//    Serial.println("ERROR: Raw reading overflow");
//  }
//  else if (status == VL6180X_ERROR_RANGEUFLOW) {
//    Serial.println("ERROR: Range reading underflow");
//  }
//  else if (status == VL6180X_ERROR_RANGEOFLOW) {
//    Serial.println("ERROR: Range reading overflow");
//  }
//  //delay(1);
  
}
