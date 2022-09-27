
//ALL TEAM MEMBERS


int motors[2][3]={[3,4,5],[6,7,8]};
#define forward 9
#define backward 10
#define RR 11
#define RL 12

void setup() {
  for(int i=0;i<2;i++){
    for(int j=0;j<3;j++){
        pinMode(motors[i][j],OUTPUT);
    }
  }
  pinMode(forward, INPUT);
  pinMode(backward, INPUT);
  pinMode(RR, INPUT);
  pinMode(RL, INPUT);
  digitalWrite(forward, HIGH);
  digitalWrite(backward, HIGH);
  digitalWrite(RR, HIGH);
  digitalWrite(RL, HIGH);
}
void loop() {
  if(digitalRead(forward) == LOW)
  {
    digitalWrite(motors[0][0], HIGH);
    digitalWrite(motors[0][1], HIGH);
    digitalWrite(motors[0][2], LOW);
  }
  else{
    digitalWrite(motors[0][0], LOW);
  }
  if(digitalRead(backward) == LOW)
  {
    digitalWrite(motors[0][0], HIGH);
    digitalWrite(motors[0][2], HIGH);
    digitalWrite(motors[0][1], LOW);
  }
  else{
    digitalWrite(motors[0][0], LOW);
  }
  if(digitalRead(RR) == LOW)
  {
    digitalWrite(motors[1][0], HIGH);
    digitalWrite(motors[1][1], HIGH);
    digitalWrite(motors[1][2], LOW);
  }
  else{
    digitalWrite(motors[1][0], LOW);
  }
  if(digitalRead(RL) == LOW)
  {
    digitalWrite(motors[1][0], HIGH);
    digitalWrite(motors[1][2], HIGH);
    digitalWrite(motors[1][1], LOW);
  }
  else{
    digitalWrite(motors[1][0], LOW);
  }
}
