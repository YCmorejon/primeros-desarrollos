import requests
import json

"""
Funciones 
"""

# Función para abrir el JSON donde están los ID de las ciudades
def abrir_json():
    with open("id.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return {city['name']: city['id'] for city in data}

# Función para pedirle datos al usuario
def pedir_usuario():
    data = abrir_json()
    while True:
        name_city = input("¿Cuál es el nombre de la ciudad que deseas información?:\n")
        
        if name_city in data:
            print("Cargando la información de tu ciudad....")
            id_city = data[name_city]
            # Params
            params = {
                "apikey": "APY_KEY",
                "id": id_city
            }
            peticion_get(params)
            break
        else:
            print("O el nombre que escribiste está incorrecto o tu ciudad no está en la base de datos. Inténtalo de nuevo.")

# Función para hacer petición GET con manejo mejorado de errores
def peticion_get(params):
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=params)
        response.raise_for_status()  # Verifica si hubo un error en la petición
        respuesta = response.json()

        # Mostrando datos
        print(f"""-La temperatura es de {respuesta['list'][0]['main']['temp'] - 273.15}°C
        -La sensación térmica es de {respuesta['list'][0]['main']['feels_like'] - 273.15}°C
        -La temperatura mínima es de {respuesta['list'][0]['main']['temp_min'] - 273.15}°C
        -La temperatura máxima es de {respuesta['list'][0]['main']['temp_max'] - 273.15}°C
        -La presión atmosférica es de {respuesta['list'][0]['main']['pressure']} hPa
        -La humedad es de {respuesta['list'][0]['main']['humidity']}%
        -La velocidad del viento es de {respuesta['list'][0]['wind']['speed']} m/s
        -La dirección del viento es de {respuesta['list'][0]['wind']['deg']}°
        -La cobertura de nubes es de {respuesta['list'][0]['clouds']['all']}%
        -La probabilidad de precipitación es de {respuesta['list'][0]['pop'] * 100}%
        -La visibilidad es de {respuesta['list'][0]['visibility']} metros
        """)

        # Verificando si existen datos de lluvia y mostrándolos
        if 'rain' in respuesta['list'][0]:
            print(f"-La cantidad de lluvia en las últimas 3 horas es de {respuesta['list'][0]['rain'].get('3h', 0)} mm")

        # Verificando si existen datos de nieve y mostrándolos
        if 'snow' in respuesta['list'][0]:
            print(f"-La cantidad de nieve en las últimas 3 horas es de {respuesta['list'][0]['snow'].get('3h', 0)} mm")

        # Mostrando descripción del clima
        print(f"-Descripción del clima: {respuesta['list'][0]['weather'][0]['description']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

# Función para interactuar con las respuestas del usuario
def res_usuario():
    while True:
        print("¿Deseas obtener información de alguna ciudad? (si/no)")
        elección = input().lower()
        respuestas_positivas = {"si", "yes", "ok"}
        respuestas_negativas = {"no", "n"}

        if elección in respuestas_positivas:
            print("Genial!")
            pedir_usuario()
        elif elección in respuestas_negativas:
            print("Gracias por tu atención. Adiós")
            break
        else:
            print("Respuesta no reconocida. Por favor, responde con 'si' o 'no'.")

# Función para información del usuario
def inf_user():
    print("Hola!\nCon este script podrás obtener información sobre las precipitaciones, el viento, la temperatura, humedad y más de las diferentes ciudades")

# Ejecutando funciones
inf_user()
res_usuario()
