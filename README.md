# Registro-PH.
Solicitante: Simon Beard
Laboratorio: Microbial Ecophysiology Lab Fundacion ciencia y vida

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
