import requests
from send_email import send_email

topic = "tesla"
api_key = "7ba478afda5c4e39ba0aa943c37b813c"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "sortBy=publishedAt&" \
       "apiKey=7ba478afda5c4e39ba0aa943c37b813c&" \
       "language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)