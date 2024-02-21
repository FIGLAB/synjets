import processing.serial.*;

Serial myPort;  // The serial port
int curr;
int smoothed;
int y;
String inBuffer;
boolean frameMoved = false;

void setup() {
  // List all the available serial ports:
  printArray(Serial.list());
  // Open the port you are using at the rate you want:
  myPort = new Serial(this, Serial.list()[2], 115200);
  size(600, 750);  // Size must be the first statement
  stroke(255);
}

void draw() {
  if(!frameMoved){
    surface.setLocation(0, 200);
    frameMoved = true;
  }
  background(255);
  while (myPort.available() > 0) {
    inBuffer = myPort.readStringUntil(10);
    if (inBuffer != null) {
      println(inBuffer);
      curr = int(float(inBuffer));
      if (curr != 0 && curr != 300) {smoothed = curr;}
    }
  }
  if (curr == 300){
    textSize(72);
    fill(0);
    text("No hand found!", 30, 300);
  }else{
    fill(0);
    rect(150,650,300,100);
    rect(200,90,200,20);
    rect(200,190,200,20);
    rect(200,290,200,20);
    rect(200,390,200,20);
    rect(200,490,200,20);
    rect(200,590,200,20);
    y = 750-int(smoothed*750/160);
    if (y>=50 && y <=130){
      fill(0,200,0);
      rect(200,90,200,20);
    }else if (y>=165 && y <=245){
      fill(0,200,0);
      rect(200,190,200,20);
    }else if (y>=265 && y <=345){
      fill(0,200,0);
      rect(200,290,200,20);
    }else if (y>=365 && y <=445){
      fill(0,200,0);
      rect(200,390,200,20);
    }else if (y>=465 && y <=545){
      fill(0,200,0);
      rect(200,490,200,20);
    }else if (y>=565 && y <=645){
      fill(0,200,0);
      rect(200,590,200,20);
    }
    fill(150);
    ellipse(300, y, 80, 40);
    
    textSize(64);
    fill(0);
    text(str(smoothed) + "mm", 0, 50);
  }
  
}
