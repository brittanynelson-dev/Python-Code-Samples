import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Article


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Keanu_Reeves"]

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info',
                  follow=True)]

    def parse(self, response):
        article = Article(
            title=response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get(),
            url=response.url,
            lastUpdated=response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        )
        yield article
