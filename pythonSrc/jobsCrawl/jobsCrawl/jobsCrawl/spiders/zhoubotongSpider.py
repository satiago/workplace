import re
import json

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from jobsCrawl.items import ZhoubotongItem 
from jobsCrawl.misc.log import info

class zhoubotongSpider(CrawlSpider):
	name = "zhoubotong"
	allowed_domains = ["jobtong.com"]
	start_urls = [
			"http://www.jobtong.com/job-list/ca217"
			]
	rules = [
			Rule(LinkExtractor(allow = ("http://www.jobtong.com/job-list/ca217(-pg[1-9]){0,1}")), follow = True, callback='parse_item')
			]

	def parse_item(self, response):
		items = []
		sel = Selector(response)
		site_label_1 = sel.css('div.job-section-body ul.job-list li')
		for site in site_label_1:
			item = ZhoubotongItem()
			item['title'] = site.css('div.job-title a').xpath('text()').extract()
			item['position'] =  site.css('div.job-title span').xpath('//a/text()').extract()
			item['company'] = site.css('p span').xpath('//a/text()').extract()
			item['address'] = site.css('p span.text-muted').xpath('text()').extract()[0]
			item['exprience'] = site.css('p span.text-muted').xpath('text()').extract()[2]
			item['education'] = site.css('p span.text-muted').xpath('text()').extract()[3]
			item['salary'] = site.css('div.right').xpath('//strong/text()').extract()
			items.append(item)

		info('parsed' + str(response))
		return items;
