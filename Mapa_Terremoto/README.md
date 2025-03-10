🌍 Mapa Interactivo de Terremotos

Este proyecto utiliza datos en tiempo real de la API de USGS para visualizar los terremotos ocurridos en la última semana en un mapa interactivo con Folium.

📌 Características

✅ Obtención de datos en tiempo real desde la API de USGS.
✅ Almacenamiento de datos en un archivo CSV.

✅ Visualización interactiva con Folium.

✅ Dos tipos de marcadores: círculos con colores según magnitud y marcadores estándar.

✅ Popups con detalles de cada terremoto.

✅ Control de capas para alternar entre visualizaciones.

🛠️ Instalación y Uso

1️-Clonar el Repositorio

git clone https://github.com/tu-usuario/mapa-terremotos.git
cd mapa-terremotos

2️-Instalar Dependencias

Asegúrate de tener Python y pip instalados, luego ejecuta:

pip install -r requirements.txt

3️-Ejecutar el Script para Obtener Datos

python datos.py

4️-Generar el Mapa

python mapa.py

5️-Abrir el Mapa en el Navegador

Abre Mapa_Base.html en tu navegador para visualizar los datos.

📂 Estructura del Proyecto

📂 mapa-terremotos

│── 📜 datos.py   # Obtiene datos de la API y los guarda en CSV

│── 📜 mapa.py    # Genera el mapa interactivo con Folium

│── 📜 datos_terremoto.csv  # Archivo con datos de los terremotos

│── 📜 README.md  # Documentación del proyecto

│── 📜 .gitignore  # Archivos a ignorar en Git

🌟 Mejoras Futuras

Agregar filtros por magnitud o ubicación.

Automatizar la actualización de datos cada cierto tiempo.

Mejorar el diseño del mapa con estilos personalizados.

🚀 ¡Contribuciones y sugerencias son bienvenidas!


