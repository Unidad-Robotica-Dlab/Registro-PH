# SOFTWARE CON INTERFAZ DE USUARIO. ASIGNAR NOMBRE EXP Y AUTOR PARA CSV E INGRESAR TIEMPO DE INTERVALO ENTRE LECTURAS.
import time
from matplotlib import pyplot as plt
import csv
import os
import datetime
import serial
import serial.tools.list_ports
from matplotlib.ticker import NullFormatter
import threading

#['303', '305', '304', '304', '304', '305', '305', '304', '304', '304'] 1.68pH
#['228', '229', '229', '229', '228', '230', '230', '229', '228', '230'] 10.01pH
#y=−0.11106666666666666x+35.444266666666664
#########################################################################################################
def seleccionar_puerto():
    puertos_disponibles = [puerto.device for puerto in serial.tools.list_ports.comports()]

    if not puertos_disponibles:
        print("No se encontraron puertos seriales disponibles.")
        return None

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
def leer_entrada():
    global continuar
    while True:
        entrada = input("Presiona 'q' para salir: ").strip().lower()
        if entrada == 'q':
            continuar = False
            break

continuar = True

##########################################################################################################

def main():
    arduino = serial.Serial(puerto, 115200, timeout=1) #windows
    time.sleep(1) # Espera a que Arduino se inicialice
    arduino.flushInput()
    print("MENU PRINCIPAL")  
    nombre_archivo = input("Escriba el nombre del .csv a guardar: ")

    print("------------------------------------------------")
    confirmar = input("Estas seguro?:")
    if confirmar == 'si':
        while True:
            print("1. Iniciar Grabacion de datos")
            print("2. Salir")
            opcionn = input("Seleccione una opción: ")
            
            if opcionn == '1':
                t_lectura = int(input("Seleccione un intervalo de tiempo (segs) entre lecturas:"))
                ruta_archivo = r'/home/manuelm/Documentos/DLAB/Registro-PH/Software/data/'+nombre_archivo+'_'+str(t_lectura)+'s_'+fecha+'.csv'
                while True:
                    iniciar = str(input("Quiere iniciar el programa? (si / no):"))
                    if iniciar =="si":
                        print("------------------------------------------------")
                        print("iniciando el programa...")
                        instruccion = 'LEER\r'
                        print("Enviando a Arduino: ", instruccion)
                        time.sleep(1)
                        arduino.write(instruccion.encode('utf-8'))
                        print("------------------------------------------------")
                        data_count = 0
                        thread_entrada = threading.Thread(target=leer_entrada)
                        thread_entrada.start()
                        try:
                            while True:
                                arduino.write(instruccion.encode('utf-8'))
                                data = arduino.readline().decode().strip()
                                archivo_csv = open(ruta_archivo, mode='a', newline='')
                                escritor_csv = csv.writer(archivo_csv)
                                escritor_csv.writerow(["tiempo","data"])
                                if data is not None and data != "":
                                    try:
                                        while continuar:
                                            data_count = data_count+1
                                            data_pH = -(0.11106666666666666*float(data))+35.444266666666664
                                            data_pH = "{:.2f}".format(data_pH)
                                            tiempo_actual = time.strftime('%H:%M:%S') 
                                            #print("Datos bruto: {:.2f}".format(float(data)))
                                            archivo_csv = open(ruta_archivo, mode='a', newline='')
                                            escritor_csv = csv.writer(archivo_csv)
                                            escritor_csv.writerow([tiempo_actual,data_pH])
                                            archivo_csv.close()
                                            print(f'pH: {data_pH}')
                                            time.sleep(t_lectura)
                                    
                                    except KeyboardInterrupt:
                                        print("Programa detenido por el usuario.")

                                    thread_entrada.join()
                                    break
                            print("------------------------------------------------")
                            time.sleep(1)
                            print("Programa terminado por el usuario, espere un momento...")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(3)
                            main()
    
    
                        except KeyboardInterrupt:
                            print("Programa detenido por el usuario.")
                                    
                           
                        
                    elif iniciar =="no":
                        print("Saliendo del programa...")
                        arduino.close()
                        break
                    else:
                        print("Error")
    
    
            elif opcionn == '2':
                print("Reiniciando...")
                arduino.close()
                time.sleep(3)
                main()
            else:
                print("Opción inválidaaa. Por favor, selecciona una opción válida.")
    if confirmar == 'no':
        print("Reiniciando...")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()
