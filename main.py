import requests
from send_email import send_email

topic = "generative AI"

api_key = "cda2b821ef5e4c6da765b67791032118"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&"\
      "apiKey=cda2b821ef5e4c6da765b67791032118&"\
      "language=en"

#made request here
request = requests.get(url)

#get dictionary with data
content = request.json()

#access the article tile and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article['title'] + "\n" \
               + article['description'] \
               +"\n" + article['url'] + 2*"\n"

body="Subject: Today AI News" + "\n"+body
body = body.encode("utf-8")
send_email(message=body)






