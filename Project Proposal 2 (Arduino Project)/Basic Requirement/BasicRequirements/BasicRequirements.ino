#include <Servo.h>

int pinOut = 3;
int degree;
int gotInput = 0;
String out = " ";

Servo serv;

void setup() {
  pinMode(pinOut, OUTPUT);
  Serial.begin(9600);
  serv.attach(3);
}

void loop() {

  while(Serial.available()) {
    char in = Serial.read();

    if(in == ';') {
      gotInput = 1;
      out = "";
      break;
      }
    
    out += in;
    if(out != "")
      degree = out.toInt();
    Serial.println(degree);

    if(degree > 180)
      degree = 0;
    
    serv.write(degree);
    delay(200);
  }
 
}
