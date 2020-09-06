from Page_locator.page_locator import PageLocator
from item_locator.item_locator import ItemLocator


class Parse:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quotes = {self.content}  by {self.author}>'

    @property
    def content(self):
        locator = ItemLocator.CONTENT
        quote = self.parent.select_one(locator).string
        return quote

    @property
    def author(self):
        locator = ItemLocator.AUTHOR
        author = self.parent.select(locator)
        return author

    @property
    def tags(self):
        locator = ItemLocator.TAGS
        tags = self.parent.select(locator)
        return [e for e in tags]
