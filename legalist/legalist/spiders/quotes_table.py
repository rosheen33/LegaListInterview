# -*- coding: utf-8 -*-
from legalist.items import QuotesItemLoader
from legalist.spiders.quotes_default import QuotesSpider


class QuotesTableSpider(QuotesSpider):
    name = 'quotes_table'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/tableful/']

    def parse(self, response):
        quote_text = response.css('table tr[style*=border] td::text')
        quote_tags = response.css('table td[style*=bottom]')

        for text, tag in zip(quote_text, quote_tags):
            yield from self.parse_quote(text, tag, response)

    def parse_quote(self, text, tag, response):
        item_loader = QuotesItemLoader()
        item_loader.add_value('url', response.url)
        item_loader.add_value('text', text.get().split('”')[0].split('“'))
        item_loader.add_value('author', text.get().split('”')[-1].strip())
        item_loader.add_value('tags', tag.css('a::text').getall())
        yield item_loader.load_item()
