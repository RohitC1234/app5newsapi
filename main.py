import requests

api_key = "7ba478afda5c4e39ba0aa943c37b813c"
url = ("https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey="
       "7ba478afda5c4e39ba0aa943c37b813c")

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


