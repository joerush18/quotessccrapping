from bs4 import BeautifulSoup
from parse.pages import Parse
from Page_locator.page_locator import PageLocator


class Soup:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def souping(self):
        locator = PageLocator.QUOTE
        quotes_tags = self.soup.select(locator)
        return [Parse(e) for e in quotes_tags]

