# -*- coding: utf-8 -*-

from itemloaders.processors import MapCompose
from legalist.items import QuotesItemLoader
from scrapy import Request
from scrapy.spiders import Spider


class QuotesSpider(Spider):
    name = 'quotes_default_redis'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    custom_settings = {
        'SCHEDULER': 'scrapy_redis.scheduler.Scheduler',
        'SCHEDULER_PERSIST': True,
        'SCHEDULER_QUEUE_CLASS': 'scrapy_redis.queue.SpiderQueue',
        'DUPEFILTER_CLASS': 'scrapy_redis.dupefilter.RFPDupeFilter',
        'ITEM_PIPELINES': {'scrapy_redis.pipelines.RedisPipeline': 300}
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css(".quote"):
            yield from self.parse_quote(quote, response)

        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page)

    def parse_quote(self, selector, response):
        item_loader = QuotesItemLoader(selector=selector)
        item_loader.add_value('url', response.url)
        item_loader.add_css('tags', '.tag *::text')
        item_loader.add_css('text', '.quote .text::text')
        item_loader.add_css('author', '[itemprop=author]::text')
        item_loader.add_css(
            'author_url', '.quote a::attr(href)', MapCompose(response.urljoin)
        )
        yield item_loader.load_item()
