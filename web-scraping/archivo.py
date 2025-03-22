import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict, List
import time
import logging

# Configuración del logging para proporcionar información detallada durante la ejecución
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Encabezados HTTP por defecto para emular un navegador real
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# URL base para la paginación de los resultados
BASE_URL = "https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
REQUEST_DELAY = 1.5  # Segundos entre solicitudes para evitar ser bloqueado
MAX_RETRIES = 3  # Número máximo de reintentos en caso de fallo

class RealEstateScraper:
    """Scraper profesional de datos inmobiliarios con manejo de errores"""
    
    def __init__(self):
        # Inicializa una sesión de requests para mantener las cookies y los encabezados
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.properties_data = []  # Lista para almacenar los datos de las propiedades
    
    def fetch_page(self, url: str) -> BeautifulSoup:
        """Obtiene y parsea una página con reintentos en caso de fallo"""
        for _ in range(MAX_RETRIES):
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
                return BeautifulSoup(response.content, 'html.parser')
            except requests.exceptions.RequestException as e:
                logging.warning(f"Error fetching {url}: {e}")
                time.sleep(REQUEST_DELAY * 2)  # Espera antes de reintentar
        return None
    
    def extract_property_data(self, property_div) -> Dict:
        """Extrae datos estructurados de una propiedad a partir del HTML"""
        data = {}
        
        # Diccionario de extractores para simplificar la extracción de datos
        extractors = {
            'Precio': ('h4', {'class': 'propPrice'}),
            'Dirección': ('span', {'class': 'propAddressCollapse'}, 0),
            'Localidad': ('span', {'class': 'propAddressCollapse'}, 1),
            'Camas': ('span', {'class': 'infoBed'}, None, 'b'),
            'Baños Completos': ('span', {'class': 'infoValueFullBath'}, None, 'b'),
            'Área': ('span', {'class': 'infoSqFt'}, None, 'b'),
            'Medios Baños': ('span', {'class': 'infoValueHalfBath'}, None, 'b')
        }
        
        for key, params in extractors.items():
            try:
                element = property_div.find(params[0], params[1])
                if len(params) > 3:
                    element = element.find(params[3])
                data[key] = element.text.strip() if element else None
            except Exception as e:
                logging.debug(f"Error extracting {key}: {e}")
                data[key] = None
        # Extracción optimizada de tamaño del lote
        lot_size = property_div.find('span', class_='featureName', string=lambda t: t and 'Lot Size' in t)
        data['Tamaño del Lote'] = lot_size.find_previous('span', class_='featureName').text if lot_size else None
        
        return data
    
    def scrape(self, max_pages: int = 3):
        """Ejecuta el scraping completo recorriendo las páginas especificadas"""
        for page in range(0, max_pages*10, 10):
            url = f"{BASE_URL}{page}.html"
            logging.info(f"Scraping page: {url}")
            
            soup = self.fetch_page(url)
            if not soup:
                continue
                
            properties = soup.find_all("div", class_="propertyRow")
            for prop in properties:
                self.properties_data.append(self.extract_property_data(prop))
            
            time.sleep(REQUEST_DELAY)  # Espera entre solicitudes para evitar ser bloqueado
    
    def save_data(self, filename: str = "real_estate_data.csv"):
        """Guarda los datos extraídos en un archivo CSV"""
        df = pd.DataFrame(self.properties_data)
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename} with {len(df)} records")

if __name__ == "__main__":
    scraper = RealEstateScraper()
    scraper.scrape()
    scraper.save_data()
