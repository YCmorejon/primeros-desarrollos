import requests
from bs4 import BeautifulSoup
import pandas as pd

# Encabezados HTTP
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

# Enlace de la web a extraer info
url = "https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"

# Realizando petición get con encabezados
respuesta = requests.get(url, headers=headers)

# Contenido de la web
contenido = respuesta.content

# Creando sopa
sopa = BeautifulSoup(contenido, "html.parser")

# Buscando los divs
busqueda = sopa.find_all("div", {"class": "propertyRow"})

# Lista para almacenar los diccionarios
lista = []
for propiedad in busqueda:
    datos = {}
    datos["Precio"] = propiedad.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
    
    # Direcciones
    direcciones = propiedad.find_all("span", {"class": "propAddressCollapse"})
    datos["Dirección"] = direcciones[0].text
    datos["Localidad"] = direcciones[1].text if len(direcciones) > 1 else None
    
    # Cantidad de camas
    try:
        datos["Camas"] = propiedad.find("span", {"class": "infoBed"}).find("b").text
    except:
        datos["Camas"] = None
        
    # Cantidad de baños
    try:
        datos["Baños Completos"] = propiedad.find("span", {"class": "infoValueFullBath"}).find("b").text
    except:
        datos["Baños Completos"] = None
    
    # Metros cuadrados   
    try:
        datos["Área"] = propiedad.find("span", {"class": "infoSqFt"}).find("b").text
    except:
        datos["Área"] = None
        
    # Baños medios   
    try:
        datos["Medios Baños"] = propiedad.find("span", {"class": "infoValueHalfBath"}).find("b").text
    except:
        datos["Medios Baños"] = None
        
    # Buscando tamaño del lote
    for tamaño in propiedad.find_all("div", {"class": "columnGroup"}):
        for grupo_caracteristicas, nombre_caracteristica in zip(tamaño.find_all("span", {"class": "featureGroup"}), tamaño.find_all("span", {"class": "featureName"})):
            if "Lot Size" in grupo_caracteristicas.text:
                datos["Tamaño del Lote"] = nombre_caracteristica.text
    
    lista.append(datos)

# Convirtiendo la lista en un Data Frame
df = pd.DataFrame(lista)

#Mostrando Data 
df
