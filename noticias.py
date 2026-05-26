import feedparser

url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"

feed = feedparser.parse(url)

for noticia in feed.entries[:3]:
    print("TÍTULO:", noticia.title)
    print("LINK:", noticia.link)
    print("RESUMEN:", noticia.summary)
    print("---")