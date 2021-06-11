# -*- coding: utf-8 -*-

from legalist.spiders.quotes_default import QuotesSpider
from scrapy import FormRequest


class QuotesLoginSpider(QuotesSpider):
    name = 'quotes_login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css("input[name=csrf_token] ::attr(value)").get()
        yield FormRequest(
            self.start_urls[0],
            formdata={
                'csrf_token': token,
                'username': 'rosheen',
                'password': 'xyz'
            },
            callback=self.parse_listing
        )

    def parse_listing(self, response):
        for quote in response.css(".quote"):
            yield from self.parse_quote(quote, response)

        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_listing)
