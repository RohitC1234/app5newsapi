import requests
from send_email import send_email

api_key = "7ba478afda5c4e39ba0aa943c37b813c"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "sortBy=publishedAt&apiKey=7ba478afda5c4e39ba0aa943c37b813c")

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body =  body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)