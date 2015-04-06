# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class RecipeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReceptenItem(Item):
    title = Field()
    url = Field()
    image = Field()
    ingredients = Field()
    description = Field()
