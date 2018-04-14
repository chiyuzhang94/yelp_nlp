# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import requests
import json
from scrapy.selector import Selector
from yelpweb.items import YelpwebItem
import math
class yelpSpider(scrapy.Spider):
	#give a name for spider
	name = "yelp"
	
	#a list to restore urls
	file = open("1104_restaurants_NewYorkNY.txt").read()
	data = json.loads(file)
	urls = []
	for business in data:
		id = business["id"]
		review_num = business["review_count"]
		page_num = int(math.ceil(review_num/20))
		if page_num > 10:
			page_num = 10
		for i in range(page_num):
			url = 'https://www.yelp.com/biz/'+id+'?start='+str(i*20)+''
			urls.append(url)

	print urls

	#define a function to initialize the recording number as the primary for each job 
	#def __init__(self):
		
	# set the spider root path
	start_urls = urls

	def parse(self, response):
		
		for sel in response.xpath('.//ul[contains(@class, "reviews")]/li'):
			items = YelpwebItem()
			rating = sel.xpath('div/div/div//img[contains(@class, "offscreen")]/@alt').extract()
			if len(rating) == 0:
				continue
			else:
				items['rating'] = rating
				items['content'] = sel.xpath('div/div[contains(@class, "review-wrapper")]/div/p/text()').extract()
				items['date'] = sel.xpath('div//span[contains(@class, "rating-qualifier")]/text()').extract()
				items['statue'] = sel.xpath('.//ul[1]/li/span/text()').extract()
				items['useful'] = sel.xpath('div/div[contains(@class, "review-wrapper")]/div[contains(@class, "review-footer clearfix")]/div//ul/li[1]/a//span[contains(@class, "count")]/text()').extract()
				items['funny'] = sel.xpath('div/div[contains(@class, "review-wrapper")]/div[contains(@class, "review-footer clearfix")]/div//ul/li[2]/a//span[contains(@class, "count")]/text()').extract()
				items['cool'] = sel.xpath('div/div[contains(@class, "review-wrapper")]/div[contains(@class, "review-footer clearfix")]/div//ul/li[3]/a//span[contains(@class, "count")]/text()').extract()
				yield items
