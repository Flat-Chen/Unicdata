# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeNewcarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    carid = scrapy.Field()
    url = scrapy.Field()
    grab_time = scrapy.Field()
    carinfo = scrapy.Field()





