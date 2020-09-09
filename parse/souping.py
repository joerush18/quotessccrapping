
from parse.pages import Parse
from Page_locator.page_locator import PageLocator


class Soup:

    def __init__(self, browser):
        self.browser = browser

    @property
    def souping(self):
        locator = PageLocator.QUOTE
        quotes_tags = self.browser.find_elements_by_css_selector(locator)
        return [Parse(e) for e in quotes_tags]

