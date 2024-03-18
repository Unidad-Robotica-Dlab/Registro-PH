{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d327c73f-1ac4-446c-99c2-4a528c04aca4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SELECCIONE PUERTO SERIAL:\n",
      "1. /dev/ttyUSB0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Seleccione el número del puerto a usar:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------------------------------------------\n",
      "MENU PRINCIPAL\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escriba el nombre del .csv a guardar:  ttt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------------------------------------------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Estas seguro?: no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reiniciando...\n",
      "MENU PRINCIPAL\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escriba el nombre del .csv a guardar:  ttt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------------------------------------------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Estas seguro?: si\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Iniciar Grabacion de datos\n",
      "2. Salir\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Seleccione una opción:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reiniciando...\n",
      "MENU PRINCIPAL\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escriba el nombre del .csv a guardar:  yyy\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------------------------------------------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Estas seguro?: si\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Iniciar Grabacion de datos\n",
      "2. Salir\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Seleccione una opción:  1\n",
      "Seleccione el tiempo total de grabacion 10\n",
      "Seleccione un intervalo de tiempo (segs) entre lecturas: 1\n",
      "Quiere iniciar el programa? (si / no): si\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------------------------------------------\n",
      "iniciando el programa...\n",
      "Enviando a Arduino:  LEER\n",
      "------------------------------------------------\n",
      "Tiempo: 2024-03-18 16:51:33, Dato: 35.44\n",
      "Tiempo: 2024-03-18 16:51:33, Dato: 35.44\n",
      "Tiempo: 2024-03-18 16:51:33, Dato: 35.44\n",
      "Tiempo: 2024-03-18 16:51:33, Dato: 35.44\n",
      "Tiempo: 2024-03-18 16:51:33, Dato: 35.44\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Presiona 'q' para salir:  q\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "salir\n",
      "------------------------------------------------\n",
      "Finalizado, espere un momento...\n",
      "------------------------------------------------\n",
      "MENU PRINCIPAL\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "from matplotlib import pyplot as plt\n",
    "import csv\n",
    "import os\n",
    "import datetime\n",
    "import serial\n",
    "import serial.tools.list_ports\n",
    "from matplotlib.ticker import NullFormatter\n",
    "import threading\n",
    "\n",
    "#['303', '305', '304', '304', '304', '305', '305', '304', '304', '304'] 1.68pH\n",
    "#['228', '229', '229', '229', '228', '230', '230', '229', '228', '230'] 10.01pH\n",
    "#y=−0.11106666666666666x+35.444266666666664\n",
    "'''\n",
    "¿configurar cuanto tiempo de grabación?\n",
    "¿cada cuanto tiempo se realiza la lectura análogo?\n",
    "¿como se guardan los datos y donde?\n",
    "'''\n",
    "#########################################################################################################\n",
    "\n",
    "def seleccionar_puerto():\n",
    "    puertos_disponibles = [puerto.device for puerto in serial.tools.list_ports.comports()]\n",
    "\n",
    "    if not puertos_disponibles:\n",
    "        print(\"No se encontraron puertos seriales disponibles.\")\n",
    "        return None\n",
    "\n",
    "    print(\"SELECCIONE PUERTO SERIAL:\")\n",
    "    for indice, puerto in enumerate(puertos_disponibles, start=1):\n",
    "        print(f\"{indice}. {puerto}\")\n",
    "\n",
    "    seleccion = 0\n",
    "    while True:\n",
    "        try:\n",
    "            seleccion = int(input(\"Seleccione el número del puerto a usar: \"))\n",
    "            print(\"------------------------------------------------\")\n",
    "            if 1 <= seleccion <= len(puertos_disponibles):\n",
    "                break\n",
    "            else:\n",
    "                print(\"Seleccion incorrecta. Intente de nuevo.\")\n",
    "        except ValueError:\n",
    "            print(\"Entrada inválida. Por favor, ingrese un número.\")\n",
    "\n",
    "    puerto_seleccionado = puertos_disponibles[seleccion - 1]\n",
    "    return puerto_seleccionado\n",
    "\n",
    "puerto = seleccionar_puerto()\n",
    "fecha = datetime.datetime.now().strftime(\"%d-%m-%Y_%H;%M;%S\")\n",
    "tiempo_actual = time.strftime('%Y-%m-%d %H:%M:%S') \n",
    "vector = []\n",
    "##########################################################################################################\n",
    "def leer_entrada():\n",
    "    global continuar\n",
    "    while True:\n",
    "        entrada = input(\"Presiona 'q' para salir: \").strip().lower()\n",
    "        if entrada == 'q':\n",
    "            continuar = False\n",
    "            break\n",
    "\n",
    "continuar = True\n",
    "\n",
    "# Iniciar el hilo para leer la entrada del usuario\n",
    "\n",
    "##########################################################################################################\n",
    "\n",
    "def main():\n",
    "    arduino = serial.Serial(puerto, 115200, timeout=1) #windows\n",
    "    time.sleep(1) # Espera a que Arduino se inicialice\n",
    "    arduino.flushInput()\n",
    "    print(\"MENU PRINCIPAL\")  \n",
    "    nombre_archivo = input(\"Escriba el nombre del .csv a guardar: \")\n",
    "    ruta_archivo = r'/home/manuelm/Documentos/DLAB/Registro-PH/Software/data/'+nombre_archivo+'.csv'\n",
    "    print(\"------------------------------------------------\")\n",
    "    confirmar = input(\"Estas seguro?:\")\n",
    "    if confirmar == 'si':\n",
    "        while True:\n",
    "            print(\"1. Iniciar Grabacion de datos\")\n",
    "            print(\"2. Salir\")\n",
    "            opcionn = input(\"Seleccione una opción: \")\n",
    "            \n",
    "            if opcionn == '1':\n",
    "                t_grabacion = input(\"Seleccione el tiempo total de grabacion\")\n",
    "                t_lectura = int(input(\"Seleccione un intervalo de tiempo (segs) entre lecturas:\"))\n",
    "                while True:\n",
    "                    iniciar = str(input(\"Quiere iniciar el programa? (si / no):\"))\n",
    "                    if iniciar ==\"si\":\n",
    "                        print(\"------------------------------------------------\")\n",
    "                        print(\"iniciando el programa...\")\n",
    "                        instruccion = 'LEER\\r'\n",
    "                        print(\"Enviando a Arduino: \", instruccion)\n",
    "                        time.sleep(1)\n",
    "                        arduino.write(instruccion.encode('utf-8'))\n",
    "                        print(\"------------------------------------------------\")\n",
    "                        data_count = 0\n",
    "                        thread_entrada = threading.Thread(target=leer_entrada)\n",
    "                        thread_entrada.start()\n",
    "                        try:\n",
    "                            while True:\n",
    "                                while data_count < int(t_grabacion):  # Continuar leyendo hasta que se lean 10 líneas\n",
    "                                    arduino.write(instruccion.encode('utf-8'))\n",
    "                                    data = arduino.readline().decode().strip()\n",
    "                                    if data is not None and data != \"\":\n",
    "                                        try:\n",
    "                                            while continuar:\n",
    "                                                data_count = data_count+1\n",
    "                                                data_pH = -(0.11106666666666666*float(data))+35.444266666666664\n",
    "                                                data_pH = \"{:.2f}\".format(data_pH)\n",
    "                                                #print(\"Datos bruto: {:.2f}\".format(float(data)))\n",
    "                                                archivo_csv = open(ruta_archivo, mode='a', newline='')\n",
    "                                                escritor_csv = csv.writer(archivo_csv)\n",
    "                                                escritor_csv.writerow([data_pH])\n",
    "                                                archivo_csv.close()\n",
    "                                                print(f'Tiempo: {tiempo_actual}, Dato: {data_pH}')\n",
    "                                                time.sleep(t_lectura)\n",
    "                                        \n",
    "                                        except KeyboardInterrupt:\n",
    "                                            print(\"Programa detenido por el usuario.\")\n",
    "\n",
    "                                        thread_entrada.join()\n",
    "                                        print(\"salir\")\n",
    "                                        break\n",
    "                                print(\"------------------------------------------------\")\n",
    "                                time.sleep(1)\n",
    "                                print(\"Programa terminado por el usuario, espere un momento...\")\n",
    "                                time.sleep(2)\n",
    "                                print(\"------------------------------------------------\")\n",
    "                                arduino.close()\n",
    "                                time.sleep(3)\n",
    "                                main()\n",
    "    \n",
    "    \n",
    "                        except KeyboardInterrupt:\n",
    "                            print(\"Programa detenido por el usuario.\")\n",
    "                                    \n",
    "                           \n",
    "                        \n",
    "                    elif iniciar ==\"no\":\n",
    "                        print(\"Saliendo del programa...\")\n",
    "                        arduino.close()\n",
    "                        break\n",
    "                    else:\n",
    "                        print(\"Error\")\n",
    "    \n",
    "    \n",
    "            elif opcionn == '2':\n",
    "                print(\"Reiniciando...\")\n",
    "                arduino.close()\n",
    "                time.sleep(3)\n",
    "                main()\n",
    "            else:\n",
    "                print(\"Opción inválidaaa. Por favor, selecciona una opción válida.\")\n",
    "    if confirmar == 'no':\n",
    "        print(\"Reiniciando...\")\n",
    "        time.sleep(3)\n",
    "        main()\n",
    "#\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e5949e6-5d4a-4ed0-a602-8b7c04bd6016",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
