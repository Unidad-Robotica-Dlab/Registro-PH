import time
from matplotlib import pyplot as plt
import csv
import os
import datetime
import serial
import serial.tools.list_ports
from matplotlib.ticker import NullFormatter
import threading
import sys
import pandas as pd

#########################################################################################################
def seleccionar_puerto():
    puertos_disponibles = [puerto.device for puerto in serial.tools.list_ports.comports()]

    if not puertos_disponibles:
        print("No se encontraron puertos seriales disponibles.")
        return None
    print("------------------------------------------------")
    print("SELECCIONE PUERTO SERIAL:")
    for indice, puerto in enumerate(puertos_disponibles, start=1):
        print(f"{indice}. {puerto}")

    seleccion = 0
    while True:
        try:
            seleccion = int(input("Seleccione el número del puerto a usar: "))
            print("------------------------------------------------")
            if 1 <= seleccion <= len(puertos_disponibles):
                break
            else:
                print("Seleccion incorrecta. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    puerto_seleccionado = puertos_disponibles[seleccion - 1]
    return puerto_seleccionado

puerto = seleccionar_puerto()
fecha = datetime.datetime.now().strftime("%d-%m-%Y")

vector = []
##########################################################################################################
def interrupcion():
    global continuar
    print("Presione 'q' para salir")
    while True:
        entrada = input("").strip().lower()
        if entrada == 'q':
            continuar = False
            break

continuar = True

##########################################################################################################
ruta_archivo2 = './/calibracion_.csv'

def main():
    m=None
    b=None
    alfa=None
    salir = False
    arduino = serial.Serial(puerto, 115200, timeout=1) #windows
    time.sleep(1) # Espera a que Arduino se inicialice
    arduino.flushInput()
    print("MENU PRINCIPAL")  
    print("Escriba el nombre del archivo a guardar (Por ejemplo: EXP1_Simon [Experimento_Autor])")
    nombre_archivo = input("Nombre del archivo: ")
    print("Estas seguro?")
    print("1. Si")
    print("2. No")
    confirmar = input("Seleccione una opción (1 o 2): ")
    print("------------------------------------------------")
    if confirmar == '1':
        while not salir:
            print("1. Iniciar Calibracion")
            print("2. Iniciar Grabacion de datos")
            print("3. Salir")
            opcionn = input("Seleccione una opción (1,2 o 3): ")

            if opcionn == '1':
                bandera = 'si'
                print("1. Iniciar nueva calibracion")
                print("2. Cargar ultima calibracion")
                opcion_cal = input("Seleccione una opción (1,2): ")
                if opcion_cal == '1':
                    print("------------------------------------------------")
                    y1 = float(input("Seleccione el pH 7: "))
                    instruccion = 'LEER\r'
                    print("Enviando a Arduino: ", instruccion)
                    time.sleep(1)
                    arduino.write(instruccion.encode('utf-8'))
                    z1 = arduino.readline().decode().strip() #7.01(y2) = 255(x2) // 4.01(y1) = 282(x1) // y=−0.1111111111111111x+35.343333333333334
                    print(z1)
                    if z1=='Ok':
                        x1 = arduino.readline().decode().strip()
                        if x1 is not None and x1 != "":
                            try:
                                x1 = float(x1)
                            except ValueError:
                                print("El string no representa un número válido:", x1)
                        else:
                            print("No se recibieron datos desde Arduino.")
                            break
                    
                    time.sleep(1)
                    y2 = float(input("Seleccione el pH 4: "))
                    instruccion = 'LEER\r'
                    print("Enviando a Arduino: ", instruccion)
                    time.sleep(1)
                    arduino.write(instruccion.encode('utf-8'))
                    z2 = arduino.readline().decode().strip() #7.01(y2) = 255(x2) // 4.01(y1) = 282(x1) // y=−0.1111111111111111x+35.343333333333334
                    print(z2)
                    if z2=='Ok':
                        x2 = arduino.readline().decode().strip()
                        if x2 is not None and x2 != "":
                            try:
                                x2 = float(x2)
                            except ValueError:
                                print("El string no representa un número válido:", x1)
                        else:
                            print("No se recibieron datos desde Arduino.")
                            break
                        
                        while True:
                            print("Estas seguro de los valores de pH ingresados?: ")
                            print("1. Si")
        
                            print("2. No") 
                            iniciar_cal = input("Seleccione una opcion (1 o 2): ")
                            if iniciar_cal =="1":
                                if x1 == x2:
                                    print("ERROR: los valores de pH ingresados son iguales")
                                    orden = 'R\r'
                                    time.sleep(1)
                                    arduino.write(orden.encode('utf-8'))
                                    salir = True
                                    break
                                else:
                                    m = (y2 - y1) / (x2 - x1) 
                                    b = y1 - m * x1
                                    time.sleep(1)
                                    print("Valores ingresados correctamente!")
                                    alfa = 0
                                    time.sleep(1)
                                    
                                    archivo_cal = open(ruta_archivo2, mode='a', newline='')
                                    escritor_cal = csv.writer(archivo_cal)
                                    escritor_cal.writerow([x1,x2,y1,y2,m,b])
                                    archivo_cal.close()
                                    break
                            if iniciar_cal =="2":
                                orden = 'R\r'
                                time.sleep(1)
                                arduino.write(orden.encode('utf-8'))
                                salir = True
                                break
                
                if opcion_cal == '2':
                    df_cal = pd.read_csv(ruta_archivo2)
                    x1= float(df_cal.columns[0])
                    x2= float(df_cal.columns[1])
                    y1= float(df_cal.columns[2])
                    y2= float(df_cal.columns[3])
                    m= float(df_cal.columns[4])
                    b= float(df_cal.columns[5])
                    print(x1,x2,y1,y2,m,b)
                    while True:
                        print("1. Ajustar calibracion")
                        opcion_ajs = input("Seleccione una opción: ")  
                        if opcion_ajs == '1':
                            y1_a = float(input("Seleccione el pH 7 ajustado: "))
                            instruccion = 'LEER\r'
                            print("Enviando a Arduino: ", instruccion)
                            time.sleep(1)
                            arduino.write(instruccion.encode('utf-8'))
                            z1_a = arduino.readline().decode().strip() #7.01(y2) = 255(x2) // 4.01(y1) = 282(x1) // y=−0.1111111111111111x+35.343333333333334
                            print(z1_a)
                            if z1_a=='Ok':
                                x1_a = arduino.readline().decode().strip()
                                if x1_a is not None and x1_a != "":
                                    try:
                                        x1_a = float(x1_a)
                                        print("el nuevo es: ",x1_a)
                                        alfa= x1-x1_a
                                        print("alfa es: " ,alfa)
                                        break
                                    except ValueError:
                                        print("El string no representa un número válido:", x1_a)
                                else:
                                    print("No se recibieron datos desde Arduino.")
                                    break
                        else:
                            print("ERROR: Debe realizar el ajuste")
            
            if opcionn == '2':

                print("------------------------------------------------")
                t_lectura = int(input("Seleccione un intervalo de tiempo (segs) entre lecturas: "))
                ruta_archivo = './/'+nombre_archivo+'_'+str(t_lectura)+'s_'+fecha+'.csv'
                
                if m == None:
                    print('ERROR: Primero debe realizar la calibración')
                    orden = 'R\r'
                    time.sleep(1)
                    arduino.write(orden.encode('utf-8'))
                    salir = True
                    break
                while True:
                    print("Quiere iniciar el programa?")
                    print("1. Si")
                    print("2. No") 
                    iniciar = input("Seleccione una opcion (1 o 2): ")
                    if iniciar =="1":
                        print("------------------------------------------------")
                        print("iniciando el programa...")
                        instruccion = 'LEER\r'
                        print("Enviando a Arduino: ", instruccion)
                        time.sleep(1)
                        arduino.write(instruccion.encode('utf-8'))
                        print("------------------------------------------------")
                        z3 = arduino.readline().decode().strip() #7.01(y2) = 255(x2) // 4.01(y1) = 282(x1) // y=−0.1111111111111111x+35.343333333333334
                        print(z3)
                        if z3 =="Ok":
                            time.sleep(1)
                            print("Hora,data")
                            data_count = 0
                            thread_entrada = threading.Thread(target=interrupcion)
                            thread_entrada.start()
                            try:
                                while True:
                                    archivo_csv = open(ruta_archivo, mode='a', newline='')
                                    escritor_csv = csv.writer(archivo_csv)
                                    escritor_csv.writerow(["tiempo","data"])
    
                                    try:
                                        while continuar:
                                            arduino.write(instruccion.encode('utf-8'))
                                            z4 = arduino.readline().decode().strip()
                                            if z4=='Ok':
                                                data = arduino.readline().decode().strip()
                                                if data is not None and data != "":
                                                    data_count = data_count+1
        
                                                    data_pH = m*(float(data)+alfa)+b 
                                                    data_pH = "{:.2f}".format(data_pH)
                                                    tiempo_actual = time.strftime('%H:%M:%S') 
                                                    archivo_csv = open(ruta_archivo, mode='a', newline='')
                                                    escritor_csv = csv.writer(archivo_csv)
                                                    escritor_csv.writerow([tiempo_actual,data_pH])
                                                    archivo_csv.close()
                                                    print(f"{tiempo_actual},{data_pH} pH\r", end="")
                                                    time.sleep(t_lectura)


                                    except KeyboardInterrupt:
                                        print("Programa detenido por el usuario.")
                                    thread_entrada.join()

                                    break
                                print("------------------------------------------------")
                                time.sleep(1)
                                print("Saliendo, espere un momento...")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print("Programa terminado")
                                time.sleep(2)
                                orden = 'R\r'
                                time.sleep(1)
                                arduino.write(orden.encode('utf-8'))
                                salir = True
                                break
        
        
                            except KeyboardInterrupt:
                                print("Programa detenido por el usuario.")
                                    
                                                   
                    elif iniciar =="2":
                        print("------------------------------------------------")
                        break
                    else:
                        print("Error")
    
    
            elif opcionn == '3':
                print("Terminado")
                arduino.close()
                time.sleep(3)
                salir = True
                

    if confirmar == '2':
        print("Reiniciando...")
        time.sleep(3)
        main()
if __name__ == "__main__":
    main()