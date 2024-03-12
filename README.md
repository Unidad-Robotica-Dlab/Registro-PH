# Proyecto: Registro-PH
## Solicitante: Simon Beard
- Laboratorio: Microbial Ecophysiology Lab Fundacion ciencia y vida

### Introduccion: 
- Maquina ElectroLab FerMac 200 capaz de controlar el pH de una solucion de forma mecanica, ademas tiene un display que muestra el pH en tiempo real.

### Requirimientos: 
- Registrar el pH mediante un esp32 y guardar los datos en una BBDD.
- [06/03/2024]
	- Almacenar los datos de la lectura en la base de datos del computador.
	- 4 Dias de fermentacion en total.
	- Sample rate por definir.
	- Menu interactivo.

### Metodologia: 
- Leer el voltaje de salida del ampop de la placa electronica de la maquina, aislar el circuito agregando otro ampop en modo diferencial y leer nuevamente el voltaje de salida mediante un esp32.

  1) Rango de operacion en voltaje del sensor PH
  2) Sistema de acoplamiento amplificador operacional
  3) Sistema de registro con una memoria SD, Cotizar un ESP32 con lector de memoria SD incluido en PCB

### Software: 
- Firmware-E_RPH_v0-1:
	- Esp32 realizando la lectura del voltaje y haciendo un promedio de los 10 subpromedios , donde cada subpromedio es el promedio de las 10 lecturas.
	- Imprime el valor en pH el cual viene de una ec. de la recta.
- Firmware-E_RPH_v0-2: -
- Software-_RPH_v0-2: -

### Notas:
- [12/02/24]
	- Maquina pH en Robotica 
- [16/02/24] : 
	- Maquina pH desarmada y con todos los implementos para medir el pH, se trajeron tres pH con diferentes valores: 1.68pH , 4pH y 10.1pH. 
- [19/02/24] : 
	- Se mide voltaje de salida en el AMPOP de la maquina y se realiza un divisor de tension. 
	- En 1.68pH = 17V ; 10.1pH = 11.1V (Vsalida ampop Maquina[model: OPA602AP])
	- En 1.68pH = 2.83V ; 10.1pH = 1.85V (con div)
	- En 1.68pH = 402 (AnalogRead) ; 10.1pH = 261 (AnalogRead)
	- Ec. Recta: y = -0.0597x+25.685

- [21/02/24] : 
	- Se quita el div de tension y se agrega un ampop en modo diferencial para aislar los circuitos. 
	- En 1.68pH = 17V ; 10.1pH = 11.1V (Vsalida ampop Maquina[model: OPA602AP])
	- En 1.68pH = 2.16V ; 10.1pH = 1.58V (con ampop Agregado [model: UA741CP])
	- En 1.68pH = 302 (AnalogRead) ; 10.1pH = 227 (AnalogRead)
	- Ec. Recta: y = -0.11226x+35.58453

- [11/03/24] : 
	- Cotizacion y dibujo de soporte del dispositivo en Inkscape


