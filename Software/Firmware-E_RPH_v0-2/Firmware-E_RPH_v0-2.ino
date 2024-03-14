
size_t numMuestras;
//ADC
#define BUFFER_SIZE 1024
int lecturas[BUFFER_SIZE];
int valores[10]; 
float vectorpH[10];
////////////////////////////
const int ADC_Carga = 34; 

int numValores = 0; 
int a=0;
int j=1;
int suma;

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
        int firstComma = data.indexOf(','); 
        int opcion = data.substring(0, firstComma).toInt(); 
        int secondComma = data.indexOf(',', firstComma + 1); 
        int t_grabacion = data.substring(firstComma + 1, secondComma).toInt();
        int thirdComma = data.indexOf(',', secondComma + 1); 
        int t_lectura = data.substring(secondComma + 1, thirdComma).toInt(); 
        int fourthComma = data.indexOf(',', thirdComma + 1); 

        if (data == "1,"+String(t_grabacion)+","+String(t_lectura)+",si") { 
          Serial.println("Ok_RPH"); 

          while(1){
            if (j<=t_grabacion) {
              for (size_t i = 0; i < t_grabacion; i++) { // Repite el parpadeo 5 veces
                lecturas[i] = analogRead(ADC_Carga);
                delayMicroseconds(t_lectura/10); // OTRA VARIABLE
              }

            for (int i = 0; i < t_grabacion; i++) {
              suma += lecturas[i];
                        
            }
            int promedio = suma/t_grabacion;

            valores[numValores] = promedio; 
            numValores++; 
            if (numValores == 10) {
              int suma2 = 0;
              for (int i = 0; i < 10; i++) {
                suma2 += valores[i];
              }

              int promedio2 = suma2 / 10;
              float pH = (-0.11226*promedio2)+35.5845;
              Serial.println(promedio2);
              j++;
              numValores = 0;
            }
            delay(t_lectura/10); 
            suma = 0;
            promedio = 0;
            lecturas[BUFFER_SIZE] = 0;
          }
          else{
            delay(1000);
          }
        }
        delay(1000); 
      }
    }
}
  


