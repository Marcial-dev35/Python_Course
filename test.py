import requests
url = "https://news.google.com/rss/search?q=tecnologia"
response = requests.get(url)
print(f"Estado de conexión: {response.status_code}")
print(f"Contenido recibido: {len(response.content)} bytes")