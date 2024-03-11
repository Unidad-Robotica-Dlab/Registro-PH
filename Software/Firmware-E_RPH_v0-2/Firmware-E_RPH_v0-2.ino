int ADC_Carga = 34;
const int numLecturas = 10; // Definir el número de lecturas a realizar
int lecturas[numLecturas]; 
int lecturas2[numLecturas]; 
int lecturas3[numLecturas]; 
int lecturas4[numLecturas]; 

int caca;
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  adcAttachPin(ADC_Carga);
  analogReadResolution(9);
  analogSetPinAttenuation(ADC_Carga,ADC_11db);
  analogSetWidth(12);
  analogSetClockDiv(1);
}

// the loop routine runs over and over again forever:
void loop() {
 int valores[10]; // Declarar un vector de 10 elementos
  int suma = 0;
  float promedio;

  // Llenar el vector con valores (esto puede ser mediante sensores, entradas digitales, etc.)
  for (int i = 0; i < 10; i++) {
    valores[i] = analogRead(ADC_Carga); // Ejemplo: lectura de un pin analógico A0
    delay(1); // Esperar un breve tiempo entre lecturas
  }

  // Sumar todos los valores del vector
  for (int i = 0; i < 10; i++) {
    suma += valores[i];
  }

  // Calcular el promedio
  promedio = suma / 10.0; // Se usa 10.0 para asegurar la división decimal

  // Imprimir el promedio de los valores
  //Serial.print("El promedio de los valores es: ");
  //Serial.println(promedio);

  // Almacenar el promedio en un vector
  static float promedios[10]; // Vector para almacenar los 10 promedios
  static int contador = 0;
  promedios[contador] = promedio;
  contador++;

  // Si hemos almacenado los 10 promedios, calculamos el promedio de los promedios
  if (contador == 10) {
    float suma_promedios = 0;
    for (int i = 0; i < 10; i++) {
      suma_promedios += promedios[i];
    }
    float promedio_de_promedios = suma_promedios / 10;
    Serial.println(promedio_de_promedios);
    float pH = (-0.0597*promedio_de_promedios)+25.685;
    Serial.println(pH);
    delay(100);

    contador = 0; // Reiniciamos el contador para el próximo conjunto de promedios
  }
  delay(10); // Esperar un segundo antes de volver a calcular el promedio
}
