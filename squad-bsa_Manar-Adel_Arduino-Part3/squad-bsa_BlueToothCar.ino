
//bluetooth controlled robot
//all team members SQUAD BSA

//left side
int speedL = 10, IN1 = 9, IN2 = 8;
//right side
int IN3 = 7, IN4 = 6, speedR = 5;

char reading;



void setup() {
  Serial.begin(9600);
  for (int i = 5; i <= 10; i++) {
    pinMode(i, OUTPUT);
  }

}
//Manar Adel
void forward()
{
  //wheels
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  //speed
  analogWrite(speedL, 150);
  analogWrite(speedR, 150);
}
//Zeina Mohamed
void backward()
{
  //wheels
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  //speed
  analogWrite(speedL, 150);
  analogWrite(speedR, 150);
}
//Habiba Ahmed
void left()
{
  //wheels
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  //speed
  analogWrite(speedL, 0);
  analogWrite(speedR, 150);
}
//Mohamed Ayman
void right()
{
  //wheels
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  //speed
  analogWrite(speedL, 150);
  analogWrite(speedR, 0);
}
//all team members
void Stop() {
  //wheels
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  //speed
  analogWrite(speedL, 0);
  analogWrite(speedR, 0);

}

//all team members
void loop() {


  if (Serial.available() > 0) {
    reading = Serial.read();

    switch (reading) {

      case 'F': forward(); break;
      case 'B': backward(); break;
      case 'R': right(); break;
      case 'L': left(); break;
      case 'S': Stop(); break;


    }
  }
}
