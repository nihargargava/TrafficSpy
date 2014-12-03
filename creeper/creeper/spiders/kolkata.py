import scrapy   

from creeper.items import trafficItem

class kolkataSpy(scrapy.Spider):
    name = "kolkata"
    allowed_domains = ["117.239.24.85"]
    start_urls = [
        "https://117.239.24.85/KTPGOVIN/Show_Programs.aspx"
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        flag = 0
        for sel in response.xpath('//table[@id="grvPrograms"]/tr'):
            item = trafficItem()
            item['date']=sel.xpath('td[1]/text()').extract()
            item['time']=sel.xpath('td[2]/text()').extract()
            item['ptype']=sel.xpath('td[3]/span/text()').extract()
            item['place']=sel.xpath('td[4]/text()').extract()
            item['details']=sel.xpath('td[5]/text()').extract()
            item['strength']=sel.xpath('td[6]/text()').extract()
            if (flag == 1) :
                yield item
            flag = 1