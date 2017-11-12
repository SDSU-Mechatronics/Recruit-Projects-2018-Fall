int red = 3;
int yellow = 5;
int green = 6;
int light = 10;
int button = 11;


void setup() {
  pinMode (red, OUTPUT);
  pinMode (yellow, OUTPUT);
  pinMode (green, OUTPUT);
  pinMode (light, OUTPUT);
  pinMode (button, INPUT);
  digitalWrite (green, HIGH);

}

void loop() {
  if (digitalRead (button) == HIGH) {
    delay (15);
    if (digitalRead (button) == HIGH) {
      delay (500); 
      changeLights ();
      delay (2000);
    }
  }
}

void changeLights () {
  
  //yellow on, green off
  digitalWrite (green, LOW);
  digitalWrite (yellow, HIGH);
  digitalWrite (red, LOW);
  delay (1500);
  
  // red on 
  digitalWrite (yellow, LOW);
  digitalWrite (green, LOW);
  digitalWrite (red, HIGH);
  digitalWrite (light, HIGH);
  delay (3000);
  digitalWrite (light, LOW);
  delay (1000);
  
  //red off, green on
  digitalWrite (yellow, LOW);
  digitalWrite (red, LOW);
  digitalWrite (green, HIGH);
  delay (2000);

}
