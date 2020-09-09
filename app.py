from selenium import webdriver

from parse.souping import Soup

chrome = webdriver.Chrome(executable_path='D:\My room\pythonProject\chromedriver.exe')
chrome.get('http://quotes.toscrape.com/search.aspx')
data = Soup(chrome)

for quote in data.souping:
    print(f'{quote.content}')
