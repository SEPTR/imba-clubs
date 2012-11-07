from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from clubs.items import ClubsItem


class ClubsSpider(BaseSpider):
    name = "clubs"
    allowed_domains = ["imba.com"]
    start_urls = ["http://www.imba.com/near-you/clubs?page=%d" % x for x in xrange(19)]


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        clubs = [c.strip() for c in hxs.select('//td[contains(@class, "views-field-display-name")]/text()').extract()]
        for club in clubs:
            item = ClubsItem()
            item["name"] = club
            items.append(item)
        return items
