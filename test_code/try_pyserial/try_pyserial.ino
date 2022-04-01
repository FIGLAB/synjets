String x;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(3);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString();
 if (x == "hello"){
  Serial.println("hi to you too");
 }else{
  Serial.println(x);
 }
}
