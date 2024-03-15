# Proyecto: Registro-PH
## Solicitante: Simon Beard
## Contacto:sbeard@cienciavida.org 
### Laboratorio: Microbial Ecophysiology Lab Fundación Ciencia y Vida

#### Introducción:
La Maquina ElectroLab FerMac 200 es capaz de controlar el pH de una solución de forma mecánica y cuenta con un display que muestra el pH en tiempo real.

#### Requerimientos:
- Registrar el pH mediante un ESP32 y guardar los datos en una base de datos.
- Fecha de solicitud: 06/03/2024
	- Almacenar los datos de la lectura en la base de datos del ordenador.
	- Duración total de la fermentación: 4 días.
	- Tasa de muestreo por determinar.
	- Implementación de un menú interactivo.

#### Metodología:
- Leer el voltaje de salida del amplificador operacional (amplificador operacional) en la placa electrónica de la máquina, aislar el circuito mediante la adición de otro amplificador operacional en modo diferencial y leer nuevamente el voltaje de salida mediante un ESP32.
  
  1) Establecer el rango de operación en voltaje del sensor de pH.
  2) Implementar un sistema de acoplamiento con amplificador operacional.
  3) Registrar el voltaje como lectura analógica en ESP32.
  4) Almacenar los datos de la lectura en la base de datos del ordenador.

#### Software:
- [Firmware-E_RPH_v0-1](https://github.com/Unidad-Robotica-Dlab/Registro-PH/blob/main/Software/Firmware-E_RPH_v0-1/Firmware-E_RPH_v0-1.ino):
	- El ESP32 realiza la lectura del voltaje y calcula un promedio de 10 subpromedios, donde cada subpromedio es el promedio de 10 lecturas.
	- Imprime el valor de pH calculado a partir de una ecuación lineal.
- [Firmware-E_RPH_v0-2](https://github.com/Unidad-Robotica-Dlab/Registro-PH/blob/main/Software/Firmware-E_RPH_v0-2/Firmware-E_RPH_v0-2.ino):
	- Agregada la comunicacion serial con Python.
- [Software_RPH_v0-2](https://github.com/Unidad-Robotica-Dlab/Registro-PH/blob/main/Software/Software_RPH_v0-2.ipynb):
	- Interfaz de usuario con Menu para guardar los datos en un csv:
 		-  Variable: Tiempo de grabacion
   		-  Variable: Tiempo entre lecturas

#### Notas:
- [12/02/24]
	- La máquina pH se encuentra en Robótica.
- [16/02/24]:
	- La máquina pH ha sido desarmada y se dispone de todos los implementos necesarios para medir el pH. Se han obtenido tres valores de pH diferentes: 1.68pH, 4pH y 10.1pH.
- [19/02/24]:
	- Se ha medido el voltaje de salida en el amplificador operacional de la máquina y se ha implementado un divisor de tensión.
	- Para 1.68pH, el voltaje de salida es de 17V; para 10.1pH, es de 11.1V (Voltaje de salida del amplificador operacional de la máquina [modelo: OPA602AP]).
	- Después del divisor de tensión, para 1.68pH, el voltaje es de 2.83V; para 10.1pH, es de 1.85V.
	- Los valores leídos analógicamente son 402 para 1.68pH y 261 para 10.1pH.
	- Ecuación de la recta: y = -0.0597x + 25.685.
- [21/02/24]:
	- Se ha eliminado el divisor de tensión y se ha agregado un amplificador operacional en modo diferencial para aislar los circuitos.
	- Para 1.68pH, el voltaje de salida es de 17V; para 10.1pH, es de 11.1V (Voltaje de salida del amplificador operacional de la máquina [modelo: OPA602AP]).
	- Después de agregar el amplificador operacional, para 1.68pH, el voltaje es de 2.16V; para 10.1pH, es de 1.58V.
	- Los valores leídos analógicamente son 302 para 1.68pH y 227 para 10.1pH.
	- Ecuación de la recta: y = -0.11226x + 35.58453.
- [11/03/24]:
	- Cotización y diseño del soporte del dispositivo en Inkscape.
