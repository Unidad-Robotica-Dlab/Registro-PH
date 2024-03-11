int ADC_Carga = 34;
const int numLecturas = 10; // Definir el número de lecturas a realizar
int lecturas[numLecturas]; 
int lecturas2[numLecturas]; 
int lecturas3[numLecturas]; 
int lecturas4[numLecturas]; 
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  /*
  adcAttachPin(ADC_Carga);
  analogReadResolution(9);
  analogSetPinAttenuation(ADC_Carga,ADC_11db);
  analogSetWidth(12);
  analogSetClockDiv(1);
  */
}

// the loop routine runs over and over again forever:
void loop() {
  int suma = 0;
  for (int i = 0; i < numLecturas; i++) {
    lecturas[i] = analogRead(ADC_Carga);// Leer el pin analógico A0
    delayMicroseconds(100); // Esperar 100 ms entre lecturas
  }

  for (int i = 0; i < numLecturas; i++) {
    suma += lecturas[i];
  }
  int promedio = suma / numLecturas;
  Serial.println(promedio);
  for (int i = 0; i < numLecturas; i++) {
    lecturas2[i] = promedio;// Leer el pin analógico A0
    delay(1); // Esperar 100 ms entre lecturas
  }

  int suma2 = 0;
  for (int i = 0; i < numLecturas; i++) {
    suma2 += lecturas2[i];
  }
  int promedio2 = suma2 / numLecturas;

  for (int i = 0; i < numLecturas; i++) {
    lecturas3[i] = promedio2;// Leer el pin analógico A0
    delay(10); // Esperar 100 ms entre lecturas
  }

  int suma3 = 0;
  for (int i = 0; i < numLecturas; i++) {
    suma3 += lecturas3[i];
  }
  int promedio3 = suma3 / numLecturas;

//Serial.print(promedio3);
//Serial.print(",");

float pH = (-0.0597*promedio3)+25.685;
//Serial.println(pH);
delay(100);
}
