import os
from dotenv import load_dotenv
from discord import Intents, Embed, Color
from discord.ext import commands


# Se carga el token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Se carga el bot
intents: Intents = Intents.default()
intents.message_content = True # NOQA
intents.reactions = True # NOQA
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print('¡El bot ha empezado a archivar!')

@bot.event
async def on_reaction_add(reaction, user):

  if user == bot.user:
    return
  
  # Modificar con el emoji que se quiera
  if reaction.emoji == '💾':
    message = reaction.message
    guild_id = message.guild.id
    channel_id = message.channel.id
    message_id = message.id

    message_link = f"https://discord.com/channels/{guild_id}/{channel_id}/{message_id}"

    # Comprobar si el mensaje tiene archivos adjuntos
    attachment_urls = [attachment.url for attachment in message.attachments]

    try:
      embed = Embed(
        title="Mensaje guardado",
        color=Color.yellow(),
      )
      embed.add_field(name="De", value=message.author.name, inline=True)
      embed.add_field(name="Fecha", value=message.created_at.strftime("%d/%m/%Y"), inline=True)
      embed.add_field(name="Enlace al mensaje", value=f"{message_link}", inline=False)
      embed.add_field(name="Contenido", value=message.content, inline=False)

      if attachment_urls:
        embed.add_field(name="Adjuntos", value="\n".join(attachment_urls), inline=False)
        await user.send(embed=embed)
      else:
        await user.send(embed=embed)
        
    except Exception as e:
      print(f"Error al enviar mensaje: {e}")

bot.run(TOKEN)

# Otro formato para enviar el mensaje privado
""" 
dm_content = (
  f"Has reaccionado a un mensaje con 💾. Aquí está el mensaje:\n\n"
  f"**De**: {message.author.name}\n"
  f"**En el canal**: {message.channel.name}\n"
  f"**Fecha**: {message.created_at}\n"
  f"**Enlace al mensaje**: {message_link}\n"
  f"**Contenido**:\n> {message.content.replace('\n', '\n> ')}"
)

if attachment_urls:
  dm_content += "\n\n**Adjuntos**:\n" + "\n".join(attachment_urls) 
"""