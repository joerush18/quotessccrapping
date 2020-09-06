from parse.souping import Soup
import requests


html_content = requests.get('http://quotes.toscrape.com').content
data = Soup(html_content)

for quote in data.souping:
    print(f'{quote.content}')


