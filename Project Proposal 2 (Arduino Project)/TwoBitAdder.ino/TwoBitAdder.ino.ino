int A = 5;
int B = 6;

int button1 = 0;
int button2 = 0;

void setup () {
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);

  digitalWrite(A, 0);
  digitalWrite(B, 0);

  Serial.begin(9600);
}

void loop () {
  
  if (digitalRead(A4))
  {
    button1++;
    if (button1 % 2)
      digitalWrite(A, 1);
    else
      digitalWrite(A, 0);
    delay(500);
  }

  if (digitalRead(A5))
  {
    button2++;
    if (button2 % 2)
      digitalWrite(B, 1);
    else
      digitalWrite(B, 0);
    delay(500);
  }
}

