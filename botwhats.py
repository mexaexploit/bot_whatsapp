import pyautogui
import webbrowser
from time import sleep

numeros_file = numeros.txt
mensajes_file = mensajes.txt

def leer_numeros():
    with open(numero_file,'r') as numeros:
        return [line.strip() for line in numeros]

def cargar_respuestas():
    respuestas = {}
    with open(mensajes_file,'r') as mensajes:
        for line in mensajes:
            key, respuesta = line.strip().split(":")
            respuestas[key.strip()] = respuesta.strip()
    return respuestas

def interactuar_con_cliente(respuestas,numero):
       url = f"https://web.whatsapp.com/send?phone={numero}"
       webbrowser.open(url)
       sleep(10)
       pyautogui.typewrite("por favor responde si o no")
       pyautogui.press("enter")
       
       respuesta_cliente = input("respuesta de cliente")
       if respuesta_cliente in respuestas:
           pyautogui.typewrite(respuestas[respuesta_cliente])
           pyautogui.press("enter") 
           
           respuesta_cliente = input("simula respuesta del cliente").strip().lower()
           
           if respuesta_cliente in respuestas:
            pyautogui.typewrite(respuestas[respuesta_cliente])
            pyautogui.press("enter")
           else:
            pyautogui.typewrite("Lo siento, no entendí tu respuesta.")
            pyautogui.press("enter")

# Cargar respuestas y números
respuestas_predefinidas = cargar_respuestas()
numeros_telefono = leer_numeros()

# Interactuar con cada cliente
for numero in numeros_telefono:
    interactuar_con_cliente(respuestas_predefinidas, numero)
    sleep(5)