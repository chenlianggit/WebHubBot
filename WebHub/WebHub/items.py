# -*- coding: utf-8 -*-

from scrapy import Item, Field


class PornVideoItem(Item):
    _id = Field()
    video_title     = Field()
    image_url       = Field()
    video_duration  = Field()
    quality_480p    = Field()
    video_views     = Field()
    video_rating    = Field()
    link_url        = Field()
    createtime      = Field()
    issave          = Field()
    local_mp4_url   = Field()
