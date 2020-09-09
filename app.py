from selenium import webdriver

from parse.souping import Soup, InvalidTagError

try:
    Location_input = input("Enter Yor chrome driver location: ")
    LOCATION = Location_input if Location_input else 'D:\My room\pythonProject\chromedriver.exe'
    author = input("Enter the author you'd like: ")
    selected_tag = input("Enter the tag: ")

    # communicating with chrome driver
    chrome = webdriver.Chrome(executable_path=LOCATION)
    chrome.get('http://quotes.toscrape.com/search.aspx')
    data = Soup(chrome)
    print(data.operations(author, selected_tag))
except InvalidTagError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Try again")
