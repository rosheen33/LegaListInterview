import scrapy
from itemloaders.processors import TakeFirst, Identity
from scrapy.loader import ItemLoader


class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()


class QuotesItemLoader(ItemLoader):
    default_item_class = QuotesItem
    default_output_processor = TakeFirst()

    tags_out = Identity()
