
//Traffic Light

#define red 3
#define yellow 4
#define green 5
#define btn 7


void setup() {
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(btn, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:

  if(digitalRead(btn)==LOW{
    digitalWrite(red,1);
    delay(500);
    digitalWrite(red,0);
  
    digitalWrite(yellow,1);
    delay(100);
    digitalWrite(yellow,0);
    delay(100);
    digitalWrite(yellow,1);
    delay(100);
    digitalWrite(yellow,0);
    delay(100);
    digitalWrite(yellow,1);
    delay(100);
    digitalWrite(yellow,0);
    delay(100);
    
    digitalWrite(green,1);
    delay(500);
    digitalWrite(green,0);
    
    
  }
  else{
    digitalWrite(red,0);
    digitalWrite(yellow,0);
    digitalWrite(green,0);
  }

}
