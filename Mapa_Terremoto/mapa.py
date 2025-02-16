import folium
import pandas as pd 

# Creando Mapa con vista global
map = folium.Map(location=[0, 0], zoom_start=2)

# Datos a Usar
df = pd.read_csv("datos_terremoto.csv", names=["Magnitud", "Tiempo", "Detalles(Url)", "Longitud", "Latitud"])
Magnitud = list(df["Magnitud"])
Tiempo = list(df["Tiempo"])
Detalles = list(df["Detalles(Url)"])
Longitud = list(df["Longitud"])
Latitud = list(df["Latitud"])

# Función para determinar el color según la magnitud del terremoto
def color_por_magnitud(magnitud):
    if magnitud >= 7.0:
        return "red"  # Muy fuerte
    elif magnitud >= 6.0:
        return "orange"  # Fuerte
    elif magnitud >= 5.0:
        return "yellow"  # Moderado
    elif magnitud >= 4.0:
        return "green"  # Débil
    else:
        return "blue"  # Muy débil

# Función para mapear colores personalizados a colores predefinidos de folium.Icon
def icon_color_por_magnitud(magnitud):
    if magnitud >= 7.0:
        return "red"
    elif magnitud >= 6.0:
        return "orange"
    elif magnitud >= 5.0:
        return "lightred"
    elif magnitud >= 4.0:
        return "green"
    else:
        return "blue"

# Capa base
fg_circle = folium.FeatureGroup(name="Terremotos (CircleMarker)", show=True)  # Mostrar esta capa por defecto
fg_marker = folium.FeatureGroup(name="Terremotos (Marker)", show=False)  # No mostrar esta capa por defecto

# Crear marcadores de círculo
for mag, tim, dett, lon, lat in zip(Magnitud, Tiempo, Detalles, Longitud, Latitud):
    color = color_por_magnitud(mag)
    icon_color = icon_color_por_magnitud(mag)
    fg_circle.add_child(
        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            popup=folium.Popup(f"<b>Magnitud:</b> {mag}<br><b>Ocurrió:</b> {tim}<br><b>Detalles:</b> <a href='{dett}' target='_blank'>Link</a>", max_width=300),
            color='black',
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            tooltip="Click para inf"
        )
    )
    fg_marker.add_child(
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(f"<b>Magnitud:</b> {mag}<br><b>Ocurrió:</b> {tim}<br><b>Detalles:</b> <a href='{dett}' target='_blank'>Link</a>", max_width=300),
            icon=folium.Icon(color=icon_color),
            tooltip="Click para inf"
        )
    )

# Añadiendo Capas       
map.add_child(fg_circle)
map.add_child(fg_marker)
map.add_child(folium.LayerControl())

# Guardando el mapa
map.save("Mapa_Base.html")
