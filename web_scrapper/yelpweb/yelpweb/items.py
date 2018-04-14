# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpwebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
    statue = scrapy.Field()
    useful = scrapy.Field()
    funny = scrapy.Field()
    cool = scrapy.Field()
