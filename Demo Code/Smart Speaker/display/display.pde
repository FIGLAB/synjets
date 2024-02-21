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
    fill(200,0,0);
    rect(200,400,200,100);
    y = 750-int(smoothed*750/160);
    if (y>=400 && y <=500){
      fill(0,200,0);
      rect(200,400,200,100);
    }
    fill(150);
    ellipse(300, y, 80, 40);
    
    textSize(64);
    fill(0);
    text(str(smoothed) + "mm", 0, 50);
  }
  
}
