import scrapy


class AhanHyperTableSpider(scrapy.Spider):

    name = 'ahanak'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['https://aradahan.com/product-category/milgerd']
    

    def start_requests(self):

        urls = [
            'https://ahanak.com/cat/rebar/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for res in response.css('table.products-table'):
            
            # for length in range(0,len(response.css('h2.product-title'))):
            #     print("[+]" + response.css('h2.product-title a::text')[length].get())
            for row in res.xpath('//tr'):
                print({
                    'code' : row.xpath('td[1]//text()').extract_first(),
                    'name': row.xpath('td[2]//text()').extract_first(),
                    'location': row.xpath('td[3]//text()').extract_first(),
                    'length': row.xpath('td[4]//text()').extract_first(),
                    'size': row.xpath('td[5]//text()').extract_first(),
                    'vahed' : row.xpath('td[6]//text()').extract_first(),
                    'weight' : row.xpath('td[7]//text()').extract_first(),
                    'price' : row.xpath('td[8]//text()').extract_first(),
                    'detail' : row.xpath('td[9]//text()').extract_first()
                })
            break