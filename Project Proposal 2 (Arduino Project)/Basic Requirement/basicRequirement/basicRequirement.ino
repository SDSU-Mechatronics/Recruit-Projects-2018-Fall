#include <Servo.h>

int pinIn = 0;
int pinOut = 3;
int degree = 0;

String output = "5";
int length = 0;
int gotInput = 0;

Servo serv;

void setup(){
  pinMode(pinOut, OUTPUT);
  Serial.begin(9600);
  serv.attach(3);
}

void loop() {
  output = "";
  while (Serial.available()){
    char input = Serial.read();
    
    if(input == ';'){
      gotInput = 1;
      output = "";
      break;
    }
    output += input;
  }
  if (output != ""){ 
    degree = output.toInt();
  }
  
  if (degree > 180){
    degree = 0;
  }
  serv.write(degree);
  delay(250);
}
