# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab1Item(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    posted_in = scrapy.Field()
    last_update = scrapy.Field()
    content = scrapy.Field()