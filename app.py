from selenium import webdriver

from parse.souping import Soup

# communicating with chrome driver
chrome = webdriver.Chrome(executable_path='D:\My room\pythonProject\chromedriver.exe')
chrome.get('http://quotes.toscrape.com/search.aspx')
data = Soup(chrome)

# selecting author from dropdown
author = input("Enter the author you'd like: ")
data.select_author(author)

# show tags available
tags = data.get_available_tags()
print('Select Tags From Here: [{}]'.format(' | '.join(tags)))

# select tag available
selected_tag = input("Enter the tags From Above: ")
data.select_tag(selected_tag)

# select button
data.search_button.click()

# getting content
for d in data.souping:
    print(d.content)
