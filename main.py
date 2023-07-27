import requests

api_key = "cda2b821ef5e4c6da765b67791032118"
url = "https://newsapi.org/v2/everything?q=AI&" \
    "from=2023-07-26&to=2023-07-26&sortBy=popularity&apiKey="\
    "cda2b821ef5e4c6da765b67791032118"

#made request here
request = requests.get(url)

#get dictionary with data
content = request.json()

#access the article tile and descriptions
for article in content["articles"]:
    print(article['title'])
    print(article['description'])







