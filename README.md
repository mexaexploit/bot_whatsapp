 Bot de Automatización de WhatsApp

Este proyecto es un bot simple de automatización de WhatsApp construido en Python utilizando `pyautogui`. Automatiza las interacciones con los clientes a través de WhatsApp Web, enviando respuestas predefinidas según su entrada.

## Características

- **Mensajería Automatizada**: Envía un mensaje pidiendo al cliente que responda con "sí" o "no".
- **Respuestas Personalizadas**: Lee respuestas predefinidas de un archivo y las envía según la entrada del cliente.
- **Múltiples Clientes**: Lee números de teléfono de un archivo y interactúa automáticamente con cada cliente.
- **Configuración Flexible**: Personaliza fácilmente los números de teléfono y mensajes a través de archivos externos (`numeros.txt` y `mensajes.txt`).

## Requisitos

- Python 3.x
- `pyautogui` para automatizar las interacciones del navegador
- `webbrowser` para abrir WhatsApp Web en el navegador predeterminado

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/mexaexploi/bot_whatsapp.git
    cd bot_whatsapp
    ```

2. Instala las dependencias:
    ```bash
    pip install pyautogui
    ```

3. Crea o actualiza el archivo `numeros.txt` con los números de teléfono a los que deseas enviar mensajes, un número por línea. Ejemplo:
    ```
    5215551234567
    5215559876543
    ```

4. Crea o actualiza el archivo `mensajes.txt` con las respuestas predefinidas, en el formato `clave:respuesta`. Ejemplo:
    ```
    si:¡Gracias por confirmar!
    no:Por favor, háganos saber si necesita asistencia.
    ```

## Uso

1. Abre WhatsApp Web en tu navegador y escanea el código QR si es la primera vez que lo usas.
2. Ejecuta el bot:
    ```bash
    python bot.py
    ```

3. El bot abrirá una nueva pestaña de WhatsApp Web para cada número de teléfono en `numeros.txt` y enviará un mensaje automatizado pidiendo una respuesta. Luego manejará la respuesta según los mensajes predefinidos en `mensajes.txt`.
