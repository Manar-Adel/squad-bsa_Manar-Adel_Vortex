
#define yellow 4
#define green 5
#define btn 7
int reading;
int count = 0;


void setup() {
  // put your setup code here, to run once:

  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(btn, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:

  reading = digitalRead(btn);

  if (reading == LOW) {

    count++;
    delay(250);

    if (count == 1) {
      digitalWrite(red, 1);
      digitalWrite(yellow, 0);
      digitalWrite(green, 0);
      
    }
    else if (count == 2) {
      digitalWrite(yellow, 1);
      digitalWrite(red, 0);
      digitalWrite(green, 0);
      
    }
    else if (count == 3) {
      digitalWrite(green, 1);
      digitalWrite(red, 0);
      digitalWrite(yellow, 0);
      
    }
    else {
      count = 0;
      digitalWrite(red, 0);
      digitalWrite(yellow, 0);
      digitalWrite(green, 0);
    }


  }



}
