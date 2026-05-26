import os
import requests
import feedparser
from groq import Groq
from dotenv import load_dotenv

# ---- CONFIGURACIÓN ----
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- 1. EXTRACCIÓN (Con disfraz de navegador) ----
# ---- 1. EXTRACCIÓN (Con disfraz mejorado) ----
def fetch_news():
    # Cambiamos a Hipertextual (tecnología, gaming y ciencia)
    url = "https://hipertextual.com/feed"
    # Un disfraz de navegador aún más convincente
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    
    print("🕵️‍♀️ Alexia está tocando la puerta del servidor...")
    response = requests.get(url, headers=headers)
    print(f"📡 Código de respuesta: {response.status_code}")
    
    feed = feedparser.parse(response.text)
    print(f"📦 Noticias encontradas: {len(feed.entries)}")
    
    return feed.entries[:3]

# ---- 2. TRANSFORMACIÓN (El Cerebro) ----
def summarize_news(title, summary):
    prompt = f"Resume esta noticia: '{title}' basándote en esto: '{summary[:500]}'. Máximo 3 líneas, tono dinámico, entusiasta y técnico para la página 'Respawn Tech'."
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---- 3. CARGA (Envío con soporte de imágenes) ----
def send_to_telegram(message, image_url=None):
    # Intentamos mandar foto primero
    if image_url:
        try:
            url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendPhoto"
            payload = {"chat_id": os.getenv('TELEGRAM_CHAT_ID'), "photo": image_url, "caption": message, "parse_mode": "HTML"}
            res = requests.post(url, data=payload)
            if res.status_code == 200:
                return # Si funcionó, cortamos aquí
        except Exception as e:
            print(f"⚠️ Falló la imagen, enviando solo texto...")
            
    # Fallback: Si no hay imagen o falló el envío anterior, mandamos solo texto
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage"
    requests.post(url, data={"chat_id": os.getenv('TELEGRAM_CHAT_ID'), "text": message, "parse_mode": "HTML"})

# ---- EJECUCIÓN PRINCIPAL ----
print("🤖 Iniciando Respawn Tech Bot (Versión Premium)...")

for article in fetch_news():
    print(f"✅ Procesando: {article.title}")
    
    # Extraemos el resumen
    resumen_ia = summarize_news(article.title, getattr(article, 'summary', ''))
    
    # Extraemos la imagen (Modo Senior: buscando en varios escondites)
    imagen = None
    if hasattr(article, 'media_content'):
        imagen = article.media_content[0]['url']
    elif hasattr(article, 'links'):
        for link in article.links:
            if 'image' in link.get('type', ''):
                imagen = link.href
                break

    # Formateamos el mensaje con HTML para Telegram
    mensaje = f"📱 <b>{article.title}</b>\n\n{resumen_ia}\n\n🔗 <a href='{article.link}'>Leer artículo completo</a>"
    
    send_to_telegram(mensaje, imagen)
    print("🚀 ¡Enviado con éxito al canal!")

print("🏁 ¡Turno terminado para el bot!")