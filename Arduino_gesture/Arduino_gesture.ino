#define oneFingerDiode 2
#define twoFingersDiode 3
#define threeFingersDiode 4
#define fourFingersDiode 5
#define fiveFingersDiode 6
char data = '0';

void setup() {
  Serial.begin(9600);
  pinMode(oneFingerDiode, OUTPUT);
  pinMode(twoFingersDiode, OUTPUT);
  pinMode(threeFingersDiode, OUTPUT);  
  pinMode(fourFingersDiode, OUTPUT);  
  pinMode(fiveFingersDiode, OUTPUT);
  disableDiodes();
}

void disableDiodes(){
  digitalWrite(oneFingerDiode, LOW);
  digitalWrite(twoFingersDiode, LOW);
  digitalWrite(threeFingersDiode, LOW);
  digitalWrite(fourFingersDiode, LOW);
  digitalWrite(fiveFingersDiode, LOW);
  delay(50);
}

void oneDiode(){
  digitalWrite(oneFingerDiode, HIGH);
  digitalWrite(twoFingersDiode, LOW);
  digitalWrite(threeFingersDiode, LOW);
  digitalWrite(fourFingersDiode, LOW);
  digitalWrite(fiveFingersDiode, LOW);
  delay(50);
}

void twoDiodes(){
  digitalWrite(oneFingerDiode, HIGH);
  digitalWrite(twoFingersDiode, HIGH);
  digitalWrite(threeFingersDiode, LOW);
  digitalWrite(fourFingersDiode, LOW);
  digitalWrite(fiveFingersDiode, LOW);
  delay(50);
}

void threeDiodes(){
  digitalWrite(oneFingerDiode, HIGH);
  digitalWrite(twoFingersDiode, HIGH);
  digitalWrite(threeFingersDiode, HIGH);
  digitalWrite(fourFingersDiode, LOW);
  digitalWrite(fiveFingersDiode, LOW);
  delay(50);
}

void fourDiodes(){
  digitalWrite(oneFingerDiode, HIGH);
  digitalWrite(twoFingersDiode, HIGH);
  digitalWrite(threeFingersDiode, HIGH);
  digitalWrite(fourFingersDiode, HIGH);
  digitalWrite(fiveFingersDiode, LOW);
  delay(50);
}

void fiveDiodes(){
  digitalWrite(oneFingerDiode, HIGH);
  digitalWrite(twoFingersDiode, HIGH);
  digitalWrite(threeFingersDiode, HIGH);
  digitalWrite(fourFingersDiode, HIGH);
  digitalWrite(fiveFingersDiode, HIGH);
  delay(50);
}

void loop() {

  while(!Serial.available());
  data = Serial.read();

  Serial.print(data);
  
  if(data == '1'){
    oneDiode();
  }
  else if(data == '2'){
    twoDiodes();
  }
  else if(data == '3'){
    threeDiodes();
  }  
  else if(data == '4'){
    fourDiodes();
  }
  else if(data == '5'){
    fiveDiodes();
  }
  
  disableDiodes();
}
