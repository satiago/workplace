# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JobscrawlItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhoubotongItem(Item):
	title = Field()       #标题
	position = Field()    #职位
	company = Field()     #公司
	address = Field()     #地址
	exprience = Field()   #工作经验
	education = Field()   #学历
	salary = Field()      #薪水
