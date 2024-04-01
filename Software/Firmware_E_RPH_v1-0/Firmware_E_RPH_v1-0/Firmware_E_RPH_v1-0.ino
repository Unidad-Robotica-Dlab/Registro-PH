
size_t numMuestras;
//ADC
#define BUFFER_SIZE 1024
int lecturas[BUFFER_SIZE];
int valores[10]; 
float vectorpH[10];
////////////////////////////
const int ADC_Carga = 35; 
int promedio;
int numValores = 0; 
int a=0;
int j=1;
int suma = 0;

void setup() {
  Serial.begin(115200); 
  adcAttachPin(ADC_Carga);
  analogReadResolution(9);
  analogSetPinAttenuation(ADC_Carga,ADC_11db);
  analogSetWidth(12);
  analogSetClockDiv(1);
  if (numMuestras > BUFFER_SIZE) {
  return;
  }

}

void loop() {

    if (Serial.available() > 0) { 
        String data = Serial.readStringUntil('\r');

          if (data == "LEER") { 
                  Serial.println("Ok");
                  for (size_t i = 0; i < 10; i++) { // Repite el parpadeo 5 veces
                    lecturas[i] = analogRead(ADC_Carga);
                    delay(100); // OTRA VARIABLE
                  }
                  for (int i = 0; i < 10; i++) {
                    suma += lecturas[i];
                              
                  }
                  promedio = suma/10;
                  Serial.println(promedio);
                  promedio = 0;
                  suma = 0;
          }
          if (data == "R") { 
            ESP.restart();
          }
          
      }
  }
  


