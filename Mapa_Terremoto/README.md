# 🌍 Mapa Interactivo de Terremotos en Tiempo Real

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-0.15.1-77B829?logo=folium&logoColor=white)
![USGS_API](https://img.shields.io/badge/USGS_API-2.5.1-important?logo=json&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green)

---

## 🌟 Características Principales

✅ **Datos en Tiempo Real**  
Actualización automática desde la API de USGS (magnitud mínima: 2.5+)

✅ **Visualización Avanzada**  
- Capas intercambiables entre marcadores estándar y círculos de calor  
- Colorización dinámica por magnitud (escala de Richter)  
- Popups informativos con detalles técnicos  

✅ **Almacenamiento Local**  
Registro histórico en CSV con timestamp de actualización  

✅ **Sistema Modular**  
- Módulo independiente para obtención de datos  
- Generación de mapas personalizable  

---

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.10+
- Conexión a internet

```bash
# Clonar repositorio
git clone https://github.com/YCmorejon/primeros-desarrollos.git
cd primeros-desarrollos/Mapa_Terremoto

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🛠️ Uso Avanzado

| Comando               | Descripción                          | Opciones                         |
|-----------------------|--------------------------------------|----------------------------------|
| `python datos.py`     | Obtener datos actualizados           | `--min-magnitude` (default: 2.5) |
| `python mapa.py`      | Generar mapa interactivo             | `--style` (circle/marker)        |
| `python main.py`      | Ejecutar flujo completo              | `--auto-update` (cada 15 min)    |

**Ejemplo de personalización:**
```python
# En mapa.py
m = folium.Map(
    location=[20, -20],  # Coordenadas iniciales
    zoom_start=3,        # Nivel de zoom
    tiles="Stamen Terrain"  # Estilo de mapa
)
```

---

## 📂 Estructura del Proyecto

| Archivo/Carpeta        | Descripción                                  |
|------------------------|----------------------------------------------|
| `datos.py`             | Obtención y procesamiento de datos de USGS  |
| `mapa.py`              | Generación del mapa interactivo con Folium  |
| `datos_terremotos.csv` | Dataset histórico con timestamps            |
| `docs/`                | Documentación técnica y capturas            |
| `config/`              | Parámetros personalizables                  |

---

## 🌐 Stack Tecnológico

| Tecnología       | Versión    | Uso Principal                 |
|------------------|------------|-------------------------------|
| Python           | 3.10+      | Lenguaje base                 |
| Folium           | 0.15.1     | Visualización geoespacial     |
| Pandas           | 2.0.3      | Manipulación de datos         |
| Requests         | 2.31.0     | Consumo de API USGS           |
| Geopandas        | 0.13.2     | Procesamiento geoespacial     |

---

## 🔮 Roadmap

- [x] Integración básica con USGS API  
- [x] Sistema de capas intercambiables  
- [ ] Filtros avanzados (magnitud/ubicación)  
- [ ] Auto-actualización programada  
- [ ] Panel de control estadístico  
- [ ] Alertas por email/SMS  

---
