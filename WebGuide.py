#Web Guide es un bot de Telegram que te ayuda a aprender sobre la web 3.0

# WebGuide
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import datetime
import asyncio
import re

# Api Del Bot en Telegram
API_KEY = "API_TOKEN"

# Bot
bot = telebot.TeleBot(API_KEY)

# Comando start
@bot.message_handler(commands=['start'])
def inicia_bot(mensaje):
    bot.reply_to(mensaje, """¡Hola! Soy WebGuide y estoy aquí para ayudarte a entender todo sobre la web 3.0. Si tienes alguna pregunta o necesitas información, no dudes en decírmelo. ¡Estoy listo para asistirte!.
   'Puedes encontrar que hace cada comando en /help'""")

# Comando help
@bot.message_handler(commands=['help'])
def ayuda_bot(mensaje):
    bot.reply_to(mensaje, """Comandos:
        /information : Brindo una pequeña información sobre el motivo de mi creación
        /notifications : Te envío una notificación para cuando quieras aprender con WebGuide
        /price : Te envío el precio de las criptomonedas más populares
        /learn : Empieza a aprender con WebGuide""")

# Comando information
@bot.message_handler(commands=['information'])
def informacion_bot(mensaje):
    bot.reply_to(mensaje, """Fui creado para proporcionar una guía accesible y comprensible sobre la web 3.0, una tecnología emergente que está transformando el internet. Mi objetivo es facilitar el acceso a información clave, responder preguntas frecuentes y ofrecer asistencia personalizada para que todos puedan entender y aprovechar las oportunidades que ofrece esta nueva era digital. ¡Ayudaré a empoderar a los usuarios para que se mantengan informados y preparados para el futuro de la web!.""")

# Comando notifications
@bot.message_handler(commands=['notifications'])
def notificar_bot(mensaje):
    if re.search(r"\d+\s\d+\s\d+", mensaje.text):
        hora_actual = datetime.datetime.now().time()
        fecha = mensaje.text.split(' ', 1)[1]
        fecha_convertida = datetime.datetime.strptime(fecha, '%H %M %S').time()
        dia = datetime.date.today()
        datetime1 = datetime.datetime.combine(dia, hora_actual)
        datetime2 = datetime.datetime.combine(dia, fecha_convertida)
        
        if datetime1 < datetime2:
            restar_horas = datetime2 - datetime1
        else:
            restar_horas = (datetime2 + datetime.timedelta(days=1)) - datetime1
        
        asyncio.run(alarma(restar_horas, mensaje))
    else:
        bot.send_message(mensaje.chat.id, "¿Cuál es la hora que quieres aprender con WebGuide?.Para enviar de forma correcta la Alarma tienes que poner /notifications seguido la hora.Ten en cuenta el formato de 24 horas.Ejemplo:14 23 02")

async def alarma(tiempo_restante, mensaje):
    segundos = tiempo_restante.total_seconds()
    bot.send_message(mensaje.chat.id, f"Ya está guardada tu alarma, será dentro de {tiempo_restante}")
    await asyncio.sleep(segundos)
    bot.send_message(mensaje.chat.id, "¡Es Hora de Aprender!")

# Comando price
@bot.message_handler(commands=['price'])
def precio_bot(mensaje):
    bot.send_message(mensaje.chat.id, "Este proceso puede tardar unos segundos")
    precios = precios_criptomonedas()
    if precios:
        respuesta = "Precios actuales de las criptomonedas más populares:\n"
        for crypto, data in precios.items():
            respuesta += f"{crypto.capitalize()}: ${data['usd']}\n"
        bot.reply_to(mensaje, respuesta)
    else:
        bot.reply_to(mensaje, "Lo siento, no pude obtener los precios de las criptomonedas en este momento.")

# Comando learn
@bot.message_handler(commands=['learn'])
def aprender_bot(mensaje):
    botones = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    botones.add(
        KeyboardButton("Web 3.0"),
        KeyboardButton("Tecnologías"),
        KeyboardButton("Privacidad"),
        KeyboardButton("Criptomonedas"),
        KeyboardButton("Beneficios"),
        KeyboardButton("Negocios"),
        KeyboardButton("Experiencia"),
        KeyboardButton("Desafíos"),
        KeyboardButton("IA")
    )
    bot.send_message(mensaje.chat.id, "¡Genial! Veamos el Auge de la Web 3.0", reply_markup=botones)
    bot.register_next_step_handler(mensaje, ejecuta_botones)

# Función para los Botones del Bot
def ejecuta_botones(message):
    respuestas = {
        "web 3.0": """Qué es la Web 3.0 y cómo difiere de la Web 2.0?
        La Web 3.0, también conocida como la web semántica o la web descentralizada, es la próxima evolución de internet que promete hacerla más inteligente, interconectada y abierta. A diferencia de la Web 2.0, que se centra en la interacción social y la creación de contenido por los usuarios, la Web 3.0 se basa en el uso de tecnologías como blockchain, inteligencia artificial y la web semántica para permitir una mayor personalización, interoperabilidad y control de los datos por parte de los usuarios.""",
        "tecnologías": """¿Cuáles son las tecnologías clave que sustentan la Web 3.0?
        Las tecnologías clave que sustentan la Web 3.0 incluyen:
        - **Blockchain**: Permite la creación de registros de datos inmutables y descentralizados.
        - **Criptomonedas**: Facilitan transacciones financieras seguras y descentralizadas.
        - **Contratos inteligentes**: Automatizan y garantizan la ejecución de acuerdos sin necesidad de intermediarios.
        - **Inteligencia Artificial (IA)**: Mejora la personalización y la capacidad de los sistemas para entender y procesar información de manera más eficiente.
        - **Web Semántica**: Permite que los datos sean comprensibles tanto por humanos como por máquinas, mejorando la interoperabilidad y el intercambio de información.""",
        "privacidad": """¿Cómo afectará la Web 3.0 a la privacidad y la seguridad en línea?
        La Web 3.0 tiene el potencial de mejorar la privacidad y la seguridad en línea al devolver el control de los datos a los usuarios. Con tecnologías como el cifrado de extremo a extremo y los sistemas de identidad descentralizados, los usuarios pueden gestionar quién tiene acceso a su información personal. Además, los datos almacenados en blockchain son más seguros y menos susceptibles a ser hackeados o manipulados.""",
        "criptomonedas": """¿Qué papel juegan las criptomonedas y los contratos inteligentes en la Web 3.0?
        Las criptomonedas facilitan transacciones económicas seguras y descentralizadas sin la necesidad de intermediarios tradicionales como los bancos. Los contratos inteligentes, que son programas autoejecutables con los términos del acuerdo directamente escritos en código, permiten automatizar y asegurar las transacciones y acuerdos entre partes sin necesidad de confiar en un intermediario.""",
        "beneficios": """¿Cuáles son los beneficios potenciales de la descentralización en la Web 3.0?
        La descentralización en la Web 3.0 ofrece varios beneficios, entre ellos:
        - **Mayor control del usuario sobre sus datos y contenidos**.
        - **Reducción de la dependencia de grandes corporaciones y servidores centralizados**.
        - **Mejora de la resistencia a la censura y a los ataques cibernéticos**.
        - **Incentivación de la innovación y la competencia**.""",
        "negocios": """¿Qué implicaciones tiene la Web 3.0 para los modelos de negocio tradicionales en internet?
        La Web 3.0 podría desafiar los modelos de negocio tradicionales basados en la centralización y el control de los datos de los usuarios. Empresas que se basan en la recopilación y monetización de datos podrían necesitar adaptarse a nuevos modelos que respeten la privacidad y den más poder a los usuarios. Además, la descentralización podría reducir los costos de intermediación y abrir nuevas oportunidades para modelos de negocio basados en la participación directa de los usuarios y las economías de tokens.""",
        "experiencia": """¿Cómo se espera que evolucione la experiencia del usuario en la Web 3.0?
        Se espera que la experiencia del usuario en la Web 3.0 sea más personalizada, intuitiva e interactiva. La inteligencia artificial permitirá servicios más adaptados a las necesidades individuales, mientras que la web semántica mejorará la búsqueda y la navegación al proporcionar resultados más relevantes y contextuales. Además, los usuarios tendrán más control sobre sus datos y cómo se utilizan.""",
        "desafíos": """¿Qué desafíos podrían surgir al adoptar la Web 3.0 a nivel global?
        Algunos de los desafíos al adoptar la Web 3.0 incluyen:
               - **Infraestructura técnica**: Necesidad de desarrollar y mantener redes descentralizadas robustas.
        - **Interoperabilidad**: Garantizar que diferentes sistemas y plataformas puedan trabajar juntos sin problemas.
        - **Regulación y cumplimiento**: Navegar por diferentes marcos regulatorios a nivel mundial.
        - **Educación y adopción**: Fomentar la comprensión y la adopción de nuevas tecnologías por parte del público general.""",
        "ia": """¿Cuál es el impacto de la inteligencia artificial en el desarrollo de la Web 3.0?
        La inteligencia artificial juega un papel crucial en la Web 3.0 al permitir que los sistemas comprendan y procesen datos de manera más efectiva y eficiente. La IA puede mejorar la personalización de los servicios, optimizar las búsquedas, detectar fraudes, y facilitar la creación de contenidos y aplicaciones más inteligentes. Además, la IA ayuda a gestionar y analizar grandes volúmenes de datos, lo cual es esencial para el funcionamiento de la web semántica y otras tecnologías de la Web 3.0."""
    }

    respuesta = respuestas.get(message.text.lower(), "No entiendo esa opción, por favor elige una de las opciones del menú.")
    bot.send_message(message.chat.id, respuesta)

# Manejando el envío de tipos de mensajes o cadenas
@bot.message_handler(content_types=['document'])
def documento_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Documentos")

@bot.message_handler(content_types=['audio'])
def audio_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Audios")

@bot.message_handler(content_types=['animation'])
def animacion_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Animaciones")

@bot.message_handler(content_types=['game'])
def juego_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Juegos")

@bot.message_handler(content_types=['photo'])
def foto_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Fotos")

@bot.message_handler(content_types=['sticker'])
def pegatina_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Pegatinas")

@bot.message_handler(content_types=['video'])
def video_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Videos")

@bot.message_handler(content_types=['video_note'])
def video_nota_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Videos-Notas")

@bot.message_handler(content_types=['voice'])
def voz_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Voz")

@bot.message_handler(content_types=['location'])
def ubicacion_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Ubicaciones")

@bot.message_handler(content_types=['contact'])
def contacto_bot(mensaje):
    bot.reply_to(mensaje, "Lo siento WebGuide por el momento no trabaja con Contactos")

@bot.message_handler(func=lambda m: True)
def mensaje_bot(mensaje):
    bot.reply_to(mensaje, "WebGuide no está aún preparada para chatear contigo.")

"""
Funciones De Comandos
"""

def precios_criptomonedas():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    parametros = {
        'ids': 'bitcoin,ethereum,ripple,binancecoin,cardano,solana,polkadot,dogecoin,litecoin,chainlink',  
        'vs_currencies': 'usd'  
    }
    response = requests.get(url, params=parametros)
    if response.status_code == 200:
        return response.json() 
    else:
        return None

# Ejecutando el bot
bot.infinity_polling()
