// Pinos dos motores
//Lado esquerdo
int in1 = 8;
int in2 = 9;

//Lado direito
int in3 = 10;
int in4 = 11;


void setup() {
  Serial.begin(9600);


  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

    // Funções de movimento
  void frente() {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }

  void re() {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }

  void esquerda() {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }

  void direita() {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }

  void pararMotores() {
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  }

}


void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    switch (comando) {
      case 'up': // Frente
        frente();
        delay(1000)
        pararMotores()
        break;
      case 'down': // Ré
        re();
        delay(1000)
        pararMotores()
        break;
      case 'left': // Esquerda
        esquerda();
        delay(1000)
        pararMotores()
        break;
      case 'right': // Direita
        direita();
        delay(1000)
        pararMotores()
        break;
    }
  }
}


