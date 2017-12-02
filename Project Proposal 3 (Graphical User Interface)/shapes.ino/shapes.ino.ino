int ptriangle = 2;
int ppenta = 3;
int pcircle = 4;
int psquare = 5;

int penta = 0;
int squar = 0;
int circle = 0;
int triangle = 0;

int input = 0;

void setup() {
  pinMode(ptriangle, OUTPUT);
  pinMode(ppenta, OUTPUT);
  pinMode(pcircle, OUTPUT);
  pinMode(psquare, OUTPUT);

  digitalWrite(ptriangle, 0);
  digitalWrite(ppenta, 0);
  digitalWrite(pcircle, 0);
  digitalWrite(psquare, 0);
  
  Serial.begin(9600);
}

void loop() {  
  if (Serial.available() > 0){
    input = Serial.read();
  }
  if (input == '1') {
    digitalWrite(ptriangle, 1);
  }
  if (input == '2') {
    digitalWrite(ppenta, 1);
  }
  if (input == '3') {
    digitalWrite(pcircle, 1);
  }
  if (input == '4') {
    digitalWrite(psquare, 1);
  }

  delay(1);
}
