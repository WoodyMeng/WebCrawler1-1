# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CochiportItem(scrapy.Item):
	date = scrapy.Field()
	ata = scrapy.Field()
	vessel = scrapy.Field()
	cargo = scrapy.Field()
	quantity = scrapy.Field()
	ie = scrapy.Field()
	agent = scrapy.Field()
