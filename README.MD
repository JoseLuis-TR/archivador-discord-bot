# Bot archivador de mensajes de discord

## Descripción

Un bot simple para discord con la intención de practicar python.

Al ser añadido a un servidor, el bot espera a que alguien reaccione a un mensaje con el emoji 💾 y le manda al usuario un embed con una copia del mensaje, los adjuntos y el enlace al mensaje original.

## Requisitos

- [Python](https://www.python.org/downloads/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Instalación

1. Clonar el repositorio
2. Instalar dependencias con `pip install -r requirements.txt`
3. Copiar el archivo `.env.example` a `.env` y modificarlo según sea necesario
4. Ejecutar el bot con `python main.py`