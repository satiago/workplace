import logging
import scrapy

def warn(msg):
	logging.warn(str(msg))

def info(msg):
	logging.info(str(msg))

def debug(msg):
	logging.debug(str(msg))
	
