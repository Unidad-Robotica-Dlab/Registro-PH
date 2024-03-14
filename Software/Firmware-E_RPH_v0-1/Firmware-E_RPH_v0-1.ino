int ADC_Carga = 34;
const int numLecturas = 10; // Definir el número de lecturas a realizar
int lecturas[numLecturas]; 
int valores[10]; 
int numValores = 0; 
int j=1;
int t_grabacion=10;
int t_lectura=200;
void setup() {
  
  Serial.begin(115200);
  adcAttachPin(ADC_Carga);
  analogReadResolution(9);
  analogSetPinAttenuation(ADC_Carga,ADC_11db);
  analogSetWidth(12);
  analogSetClockDiv(1);
}

void loop() {
  int suma = 0;

  if (j<=t_grabacion) {
    for (int i = 0; i < numLecturas; i++) {
      lecturas[i] = analogRead(ADC_Carga);//
      delayMicroseconds(t_lectura); // Esperar 100 ms entre lecturas
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
      Serial.println(j);
      j++;
      numValores = 0;
    }
    delay(t_lectura);
    }
  else{
  Serial.println("Termino");
  delay(1000);
  }
}
