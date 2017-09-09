# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import logging
import csv
import os


class ReleasespiderSpider(scrapy.Spider):
    name = "releaseSpider"
    allowed_domains = ["homers-smut.tumblr.com","reed-emissions.tumblr.com","reedrelieves.tumblr.com"]
    start_urls = ['http://homers-smut.tumblr.com/archive','reed-emissions.tumblr.com/archive']

    def start_requests(self):
        logging.info('releaseSpider start request begin')
