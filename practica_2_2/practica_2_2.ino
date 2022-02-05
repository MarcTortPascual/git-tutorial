int LED = 3;
int BRILLO;
int POT=0;
void setup() {
  pinMode(LED,OUTPUT);

}

void loop() {
  BRILLO=analogRead(POT);
  if (BRILLO>0 and BRILLO<100){
    digitalWrite(0,HIGH);
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(8,LOW);
    
    }
  else if(BRILLO>100 and BRILLO<300){
    digitalWrite(2,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(8,LOW);
    digitalWrite(0,LOW);
    }
  else if(BRILLO>300 and BRILLO<500){
    digitalWrite(4,HIGH);
    digitalWrite(8,LOW);
    digitalWrite(2,LOW);
    digitalWrite(6,LOW);
    digitalWrite(0,LOW);
    }
  else if(BRILLO>500 and BRILLO<700){
    digitalWrite(6,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(2,LOW);
    digitalWrite(8,LOW);
    digitalWrite(0,LOW);
    
    }
  else if(BRILLO>700 and BRILLO<900){
    digitalWrite(8,HIGH);
    digitalWrite(6,LOW);
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(0,LOW);
    }

}
