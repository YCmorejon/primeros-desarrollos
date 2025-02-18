import requests
from datetime import datetime

# URL
URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

#Función para construir un txt
def construyendo_txt(magnitud, tiempo, url_inf,latitud,logitud):
	with open("datos_terremoto.csv", "a") as txt:
		txt.write(f"{magnitud},{tiempo}, {url_inf},{latitud},{logitud}\n")
	

# Función para extraer datos del api
def extraer_datos(respuesta_json, i):
    feature_properties = respuesta_json["features"][i]["properties"]
    feature_geometry = respuesta_json["features"][i]["geometry"]
    magnitud = feature_properties["mag"]
    tiempo = datetime.fromtimestamp(feature_properties["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
    url_inf = feature_properties["url"]
    longitud = feature_geometry["coordinates"][0]
    latitud = feature_geometry["coordinates"][1]
    return magnitud, tiempo, url_inf,longitud,latitud

# Respuesta de petición get
try:
    response = requests.get(URL)
    response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
    respuesta_json = response.json()

    # Datos extraidos del api
    for i in range(0, respuesta_json["metadata"]["count"]):  # Mostrar solo los primeros 10
        magnitud, tiempo, url_inf, longitud, latitud= extraer_datos(respuesta_json, i)
        
        # Comprobando la respuesta del get
        df = construyendo_txt(magnitud, tiempo, url_inf, longitud,latitud)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud HTTP: {e}")
except KeyError as e:
    print(f"Error: La clave {e} no existe en el JSON.")
except ValueError as e:
    print(f"Error: Valor inválido en los datos (por ejemplo, tiempo no válido).{e}")
except Exception as e:
    print(f"Error inesperado: {e}")
