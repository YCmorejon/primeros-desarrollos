# 🏠 RealEstateScraper - Analizador de Mercado Inmobiliario

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Dependencias](https://img.shields.io/badge/Dependencias-Requests%20%7C%20BeautifulSoup%20%7C%20Pandas-orange)](requirements.txt)

Herramienta automatizada para extracción y análisis de datos inmobiliarios en tiempo real.

## 📌 Descripción del Proyecto
Sistema de scraping avanzado que recopila y organiza información clave de propiedades en venta, permitiendo:
- Detección de tendencias de precios
- Análisis comparativo de características
- Identificación de oportunidades de inversión

Extrae automáticamente datos de múltiples páginas y genera reportes listos para análisis.

## 🚀 Características Principales
- Extracción multi-página con throttling inteligente
- 8+ campos de datos por propiedad
- Manejo robusto de errores y reintentos
- Exportación automática a CSV
- Configuración personalizable

## 📦 Instalación
1. Clona el repositorio:
```bash
git clone https://github.com/YCmorejon/RealEstateScraper.git
cd RealEstateScraper
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🛠 Uso Básico
```python
from scraper import RealEstateScraper

# Inicializar scraper
scraper = RealEstateScraper()

# Ejecutar scraping (3 páginas)
scraper.scrape(max_pages=3)

# Guardar datos
scraper.save_data("propiedades.csv")
```

## 🔍 Datos Recopilados
| Campo               | Ejemplo              | Descripción                  |
|---------------------|----------------------|------------------------------|
| Precio              | $350,000            | Precio listado               |
| Dirección           | 123 Main St         | Ubicación exacta             |
| Camas               | 3                   | Número de habitaciones       |
| Área                | 1800 sqft           | Metros cuadrados construidos |
| Tamaño del Lote     | 0.5 acres           | Dimensiones del terreno      |

## ⚙️ Detalles Técnicos
- **Arquitectura:** POO con separación de responsabilidades
- **Seguridad:** Headers personalizados y delays aleatorios
- **Rendimiento:** Sesiones HTTP persistentes
- **Mantenibilidad:** Type hints y logging integrado

## 🤝 Cómo Contribuir
1. Haz fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios
4. Haz push de los cambios (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 🎓 Reconocimientos
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Parsing HTML/XML
- [Pandas](https://pandas.pydata.org/) - Manipulación de datos
- [Requests](https://requests.readthedocs.io/) - Cliente HTTP
```
