# -*- coding:utf-8 -*-

from lxml import etree
import scrapy
import re
import json



# https://m.ctrip.com/restapi/soa2/30668/search

class XiechengdemoSpider(scrapy.Spider):
    name = "xiechengDemo"
    allowed_domains = ["hotels.ctrip.com"]
    start_urls = ["https://hotels.ctrip.com/hotels/list?city=1"]
    index =1
    
    # base_url = "https://hotels.ctrip.com/hotel"

    def parse(self, response):
        # print(response.xpath('//script[@id="__MFE_leftSideNavLayer_DATA__"]').extract()[0])
        with open('data.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        # if self.index <0:
        #     self.index += 1
        #     yield scrapy.Request(url=self.start_urls[0][:-1]+str(self.index),callback=self.parse)
         
        pass


