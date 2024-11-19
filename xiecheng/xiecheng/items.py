# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiechengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HotelInfoItem(scrapy.Item):
    id = scrapy.Field()                          # INTEGER
    name = scrapy.Field()                        # VARCHAR
    comment_num = scrapy.Field()                 # VARCHAR
    price = scrapy.Field()                       # VARCHAR
    city = scrapy.Field()                        # VARCHAR
    area = scrapy.Field()                        # VARCHAR
    address = scrapy.Field()                     # VARCHAR
    lat = scrapy.Field()                         # VARCHAR (纬度)
    lng = scrapy.Field()                         # VARCHAR (经度，这里可能是个笔误，通常使用 'lng' 表示经度)
    rating = scrapy.Field()                      # VARCHAR
    environmental_rating = scrapy.Field()        # VARCHAR
    health_rating = scrapy.Field()               # VARCHAR
    service_rating = scrapy.Field()              # VARCHAR
    facility_rating = scrapy.Field()             # VARCHAR
    tag = scrapy.Field()                         # VARCHAR

class CommentItem(scrapy.Item):
    id = scrapy.Field()                          # INTEGER
    comment_text = scrapy.Field()                # VARCHAR
    location = scrapy.Field()                    # VARCHAR
