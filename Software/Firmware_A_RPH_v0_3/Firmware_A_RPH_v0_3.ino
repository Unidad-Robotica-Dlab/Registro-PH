int ADC_Carga = 34;
const int numLecturas = 10; // Definir el número de lecturas a realizar
int lecturas[numLecturas]; 
int valores[10]; 
int numValores = 0; 


void setup() {
  
  Serial.begin(9600);

}

void loop() {
  int suma = 0;
  //10.1pH = 261
  //1.68pH = 399 - 405 = 402
  for (int i = 0; i < numLecturas; i++) {
    //lecturas[i] = random(398, 410);
    lecturas[i] = analogRead(ADC_Carga);//
    //Serial.print(lecturas[i]);
    //Serial.print(",");
    delayMicroseconds(100); // Esperar 100 ms entre lecturas
  }
  //Serial.println("");
  for (int i = 0; i < numLecturas; i++) {
    suma += lecturas[i];
  }
  int promedio = suma/numLecturas;
  valores[numValores] = promedio; 
  numValores++; 
  
  if (numValores == 10) {
    int suma2 = 0;
    for (int i = 0; i < 10; i++) {
      suma2 += valores[i];
    }
    int promedio2 = suma2 / 10;
    Serial.print(promedio2);
    Serial.print(",");
    float pH = (-0.11226*promedio2)+35.5845;
    Serial.println(pH);
    numValores = 0;
  }

  delay(100);
}
