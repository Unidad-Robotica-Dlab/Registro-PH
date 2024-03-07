# Proyecto: Registro-PH
## Solicitante: Simon Beard
- Laboratorio: Microbial Ecophysiology Lab Fundacion ciencia y vida

### Introduccion: 
- Maquina capaz de mostrar el pH de una solucion.

### Requirimientos: 
- 4 Dias de fermentacion en total.
- Almacenar los datos de la lectura en la base de datos del computador.
- Sample rate por definir.
- Menu interactivo.

### Metodologia: 
- Aislar maquina a traves de un amp.op y leer el voltaje bruto del sensor de pH para luego incorporarlo en el esp32. De esta forma se registran los datos en tiempo real.

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
