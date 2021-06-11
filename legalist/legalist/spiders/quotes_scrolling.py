# -*- coding: utf-8 -*-
import json

from itemloaders.processors import MapCompose
from legalist.items import QuotesItemLoader
from scrapy.spiders import Spider


class QuotesScrollingSpider(Spider):
    name = 'quotes_scrolling'
    allowed_domains = ['quotes.toscrape.com']

    base_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [base_url.format('1')]

    def parse(self, response):
        json_data = json.loads(response.text)

        for quote in json_data['quotes']:
            yield from self.parse_quote(quote, response)

        if json_data['has_next']:
            yield response.follow(self.base_url.format(json_data['page'] + 1))

    def parse_quote(self, quote, response):
        item_loader = QuotesItemLoader()
        item_loader.add_value('url', response.url)
        item_loader.add_value('text', quote['text'])
        item_loader.add_value('tags', quote['tags'])
        item_loader.add_value('author', quote['author']['name'])
        item_loader.add_value(
            'author_url', quote['author']['goodreads_link'], MapCompose(response.urljoin)
        )
        yield item_loader.load_item()
