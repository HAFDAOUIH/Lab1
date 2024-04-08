import os
import scrapy

from ..items import Lab1Item


class AddustourspiderSpider(scrapy.Spider):
    name = "addustourspider"
    allowed_domains = ["www.addustour.com"]
    start_urls = ["https://www.addustour.com/categories/8-قضايا-واراء?type=archive"]
    opinion_links_limit = 500  # Limit of opinion links to scrape

    def __init__(self):
        self.opinion_links_scraped = 0

    def parse(self, response):
        opinion_links = response.css('div.opinion_articles a.opinion_link')
        for link in opinion_links:
            if self.opinion_links_scraped >= self.opinion_links_limit:
                os.exit(0)
            hrefs = link.attrib['href']
            self.opinion_links_scraped += 1
            yield response.follow(hrefs, callback=self.parse_content)

        next_page_links = response.css('div.pagination ul.pager li a::attr(href)').extract()
        for next_page_link in next_page_links:
            yield response.follow(next_page_link, callback=self.parse)

    def parse_content(self, response):
        item = Lab1Item()

        item['author'] = response.css('h4.avatar_name::text').get()
        item['title'] = response.css('h1.headingInfo_title::text').get()
        item['title'] = item['title'].strip() if item['title'] else None

        item['posted_in'] = response.css('div.timeDate span.timeDate_element:nth-of-type(1) time::text').get()
        item['last_update'] = response.css('div.timeDate span.timeDate_element:nth-of-type(2) time::text').get()

        content_paragraphs = response.css('div.box-wrapper p ::text').getall()
        item['content'] = ' '.join(content_paragraphs)

        yield item
