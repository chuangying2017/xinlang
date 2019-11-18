# -*- coding: utf-8 -*-
import scrapy


class XiechenSpider(scrapy.Spider):
    name = 'xiechen'
    allowed_domains = ['ctrip.com']
    start_urls = ['http://ctrip.com/']

    def parse(self, response):
        self.logger.debug(response)
