# -*- coding: utf-8 -*-

from legalist.spiders.quotes_default import QuotesSpider


class QuotesRandomSpider(QuotesSpider):
    name = 'quotes_random'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    custom_settings = {
        'ITEM_PIPELINES': {'legalist.pipelines.LegalistPipeline': 1}
    }

    def parse(self, response):
        for quote in response.css(".quote"):
            yield from self.parse_quote(quote, response)
