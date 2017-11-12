
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  int num;
  int current = 0;
  while (current <= 63) {

    num = current;
    if ((num - 32) >= 0) {
      analogWrite(11, 255);
      num = num - 32;
    }
    if ((num - 16) >= 0) {
      analogWrite(10, 255);
      num = num - 16;
    }
    if ((num - 8) >= 0) {
      analogWrite(9, 255);
      num = num - 8;
    }
    if ((num - 4) >= 0) {
      analogWrite(6, 255);
      num = num - 4;
    }
    if ((num - 2) >= 0) {
      analogWrite(5, 255);
      num = num - 2;
    }
    if ((num - 1) >= 0) {
      analogWrite(3, 255);
      num = num - 1;
    }
    delay(500);
    analogWrite(3, 0);
    analogWrite(5, 0);
    analogWrite(6, 0);
    analogWrite(9, 0);
    analogWrite(10, 0);
    analogWrite(11, 0);
    current++;
  }
}
