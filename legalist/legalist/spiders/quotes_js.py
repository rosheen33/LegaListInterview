# -*- coding: utf-8 -*-
import json

from legalist.spiders.quotes_scrolling import QuotesScrollingSpider


class QuotesJSSpider(QuotesScrollingSpider):
    name = 'quotes_js'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        script = response.xpath(
            '//script[contains(., "var data =")]/text()'
        ).re_first('var data = (\[[\w\W]*?\]);')
        json_data = json.loads(script)

        for quote in json_data:
            yield from self.parse_quote(quote, response)

        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page)
