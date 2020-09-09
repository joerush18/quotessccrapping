from typing import List
from selenium.webdriver.support.ui import Select

from parse.pages import Parse
from Page_locator.page_locator import PageLocator


class Soup:

    def __init__(self, browser):
        self.browser = browser

    # getting content Quotes
    @property
    def souping(self) -> List[Parse]:
        locator = PageLocator.QUOTE
        quotes_tags = self.browser.find_elements_by_css_selector(locator)
        return [Parse(e) for e in quotes_tags]

    # author select from dropdown / pass through  user input
    @property
    def author_dropdown(self) -> Select:
        locator = PageLocator.AUTHOR_DROPDOWN
        author = self.browser.find_element_by_css_selector(locator)
        return Select(author)

    def select_author(self, author_name):
        self.author_dropdown.select_by_visible_text(author_name)

    # tags Activity getting / updating
    @property
    def tags_dropdown(self):
        locator = PageLocator.TAG_DROPDOWN
        tags = self.browser.find_element_by_css_selector(locator)
        return Select(tags)

    def get_available_tags(self):
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tags_name):
        self.tags_dropdown.select_by_visible_text(tags_name)

    # submit button work
    @property
    def search_button(self):
        locator = PageLocator.SUBMIT_BUTTON
        return self.browser.find_element_by_css_selector(locator)
