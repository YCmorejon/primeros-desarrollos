```markdown
# 🤖 WebGuide - Tu Asistente de Web 3.0 en Telegram

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram_Bot-2CA5E0?logo=telegram&logoColor=white)
![CoinGecko](https://img.shields.io/badge/CoinGecko_API-4C8CBF?logo=coingecko&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green)

---

## 📌 Características Principales

✅ **Guía Educativa de Web 3.0**  
Conceptos fundamentales y tecnologías clave en 9 categorías organizadas  

✅ **Seguimiento de Criptomonedas**  
Precios en tiempo real de 50+ activos digitales  

✅ **Sistema de Notificaciones**  
Alertas personalizadas para sesiones de aprendizaje  

✅ **Interfaz Interactiva**  
Menús con botones para navegación intuitiva  

✅ **Protección de Contenido**  
Filtrado de archivos no soportados y comandos inválidos  

---

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.10+
- Cuenta de desarrollador en Telegram

### Pasos de Instalación
```bash
# Clonar repositorio
git clone https://github.com/YCmorejon/primeros-desarrollos.git
cd primeros-desarrollos/WebGuide

# Instalar dependencias
pip install -r requirements.txt

# Configurar ambiente
cp config.example.py config.py
```

### Configuración del Bot
1. Crea tu bot con [BotFather](https://core.telegram.org/bots#6-botfather)
2. Edita `config.py`:
```python
API_KEY = "tu_api_key_telegram"  # Obligatorio
CRYPTO_CURRENCIES = ["bitcoin", "ethereum"]  # Personalizable
```

### Ejecución
```bash
python bot.py
```

---

## 📋 Comandos Disponibles

| Comando           | Descripción                                  | Ejemplo                |
|-------------------|----------------------------------------------|------------------------|
| `/start`          | Mensaje de bienvenida                        | `/start`               |
| `/help`           | Lista de comandos disponibles                | `/help`                |
| `/price [cripto]` | Consultar precio de criptomoneda             | `/price bitcoin`       |
| `/learn`          | Menú interactivo de aprendizaje              | `/learn blockchain`    |
| `/notify [hora]`  | Configurar alertas diarias                   | `/notify 09:00`        |

---

## 🧠 Módulo de Aprendizaje

### Categorías Disponibles
1. Fundamentos de Web 3.0
2. Arquitectura Blockchain
3. Contratos Inteligentes
4. DeFi (Finanzas Descentralizadas)
5. NFTs y Metaverso
6. Privacidad y Seguridad
7. Gobernanza DAO
8. Mercado Cripto
9. Impacto de la IA

```python
# Ejemplo de estructura de contenido
learning_modules = {
    "blockchain": {
        "title": "Tecnología Blockchain",
        "content": "Sistema descentralizado de registros...",
        "resources": ["https://ethereum.org/es/"]
    }
}
```

---

## 🌐 Integración con APIs

### CoinGecko API
```python
def get_crypto_prices():
    """Obtiene precios actualizados desde CoinGecko"""
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(config.CRYPTO_CURRENCIES),
        'vs_currencies': 'usd',
        'include_market_cap': 'true'
    }
    response = requests.get(url, params=params)
    return response.json()
```

---

## 🛠️ Stack Tecnológico

| Tecnología         | Versión    | Uso Principal                |
|--------------------|------------|------------------------------|
| Python             | 3.10+      | Lenguaje base                |
| python-telegram-bot| 20.3       | Interacción con Telegram API |
| Requests           | 2.31.0     | Consumo de APIs externas     |
| Asyncio            | 3.4.3      | Programación asíncrona       |
| Pytest             | 7.4.0      | Pruebas unitarias            |

---

## 🔮 Roadmap

- [ ] Integración con OpenAI GPT-4
- [ ] Sistema de logros y badges
- [ ] Soporte multilingüe (ES/EN)
- [ ] Panel de control administrativo

---

## 🤝 Cómo Contribuir

1. Haz fork del proyecto
2. Crea tu feature branch:
```bash
git checkout -b feature/nueva-funcionalidad
```
3. Realiza y testea tus cambios
4. Envía Pull Request con:
- Descripción detallada
- Capturas de pantalla (opcional)
- Tests actualizados

**¡Las contribuciones son bienvenidas!** 🚀

---

_¿Preguntas o sugerencias? ¡Abre un [issue](https://github.com/YCmorejon/primeros-desarrollos/issues) o contáctame en [LinkedIn](https://linkedin.com/in/tuperfil)!_
```
