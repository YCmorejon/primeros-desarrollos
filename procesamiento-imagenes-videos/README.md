# 🎥 Sistema de Detección de Movimiento con OpenCV

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-5C3EE8?logo=opencv&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0.3-150458?logo=pandas&logoColor=white)

---

## 🌟 Características Principales

✅ **Detección Precisa**  
- Fondo adaptativo con actualización dinámica  
- Filtrado de ruido mediante desenfoque gaussiano  
- Umbralización automática con método de Otsu  
- Detección de contornos con área mínima configurable  

✅ **Registro de Actividad**  
- CSV estructurado con timestamps precisos  
- Marcado visual con rectángulos en tiempo real  
- Interfaz minimalista centrada en la detección  

✅ **Configuración Flexible**  
- Sensibilidad ajustable (área mínima de detección)  
- Soporte para múltiples fuentes de video  
- Exportación de datos en formatos estándar  

---

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.10+
- Cámara web funcional

```bash
# Clonar repositorio
git clone https://github.com/YCmorejon/primeros-desarrollos.git
cd primeros-desarrollos/procesamiento-imagenes-videos

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🛠️ Uso Avanzado

| Comando               | Descripción                          | Opciones                         |
|-----------------------|--------------------------------------|----------------------------------|
| `python webcam.py`    | Iniciar detección con cámara web     | `--min-area` (default: 1000)     |
| `python video.py`     | Procesar archivo de video            | `--input video.mp4`              |
| `python stats.py`     | Generar reportes estadísticos        | `--output reporte.pdf`           |

**Ejemplo de personalización:**
```python
# En webcam.py
detector = MotionDetector(
    min_area=1500,       # Área mínima para detección
    blur_ksize=(21, 21), # Tamaño del kernel de desenfoque
    threshold=25         # Umbral de detección
)
```

---

## 📂 Estructura del Proyecto

| Archivo/Carpeta        | Descripción                                  |
|------------------------|----------------------------------------------|
| `webcam.py`            | Detección en tiempo real con cámara web      |
| `video.py`             | Procesamiento de archivos de video           |
| `Times.csv`            | Registro histórico de eventos de movimiento  |
| `docs/`                | Documentación técnica y capturas             |
| `config/`              | Parámetros personalizables                   |

---

## 🌐 Stack Tecnológico

| Tecnología       | Versión    | Uso Principal                 |
|------------------|------------|-------------------------------|
| Python           | 3.10+      | Lenguaje base                 |
| OpenCV           | 4.8.0      | Procesamiento de video        |
| Pandas           | 2.0.3      | Manejo de datos temporales    |
| NumPy            | 1.24.3     | Operaciones matriciales       |

---

## 🔮 Roadmap

- [x] Detección básica con cámara web  
- [x] Exportación de datos a CSV  
- [ ] Integración con notificaciones push  
- [ ] Soporte para múltiples cámaras  
- [ ] Interfaz gráfica de usuario (GUI)  
- [ ] Análisis avanzado de patrones  

---
