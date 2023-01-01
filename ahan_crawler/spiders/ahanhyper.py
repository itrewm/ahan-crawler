import scrapy
import requests

class AhanHyperTableSpider(scrapy.Spider):

    name = 'ahanhyper'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['https://aradahan.com/product-category/milgerd']
    type = ""

    def start_requests(self):

        urls = [
            'milgerd@ajdar@https://ahanhyper.com/product-category/%d9%85%db%8c%d9%84%da%af%d8%b1%d8%af/',
            # 'milgerd@sade@https://ahanhyper.com/product-category/%d9%85%db%8c%d9%84%da%af%d8%b1%d8%af/%d9%85%db%8c%d9%84%da%af%d8%b1%d8%af-%d8%b3%d8%a7%d8%af%d9%87/'
            
        ]

        tir_ahan = [
            # 'sade@https://ahanhyper.com/product-category/%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86/%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86-%d9%86%d8%b1%d9%85%d8%a7%d9%84/'
            # 'hash@https://ahanhyper.com/product-category/%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86/%d9%87%d8%a7%d8%b4/'
        ]

        profil = [
            'sanati@https://ahanhyper.com/product-category/%d9%be%d8%b1%d9%88%d9%81%db%8c%d9%84/%d9%be%d8%b1%d9%88%d9%81%db%8c%d9%84-%d8%b5%d9%86%d8%b9%d8%aa%db%8c/'
        ] 

        varagh = [
            # 'siah@https://ahanhyper.com/product-category/%d9%88%d8%b1%d9%82/%d9%88%d8%b1%d9%82-%da%af%d8%b1%d9%85/%d9%88%d8%b1%d9%82-%d8%b3%db%8c%d8%a7%d9%87/'
            #'roghani@https://ahanhyper.com/product-category/%d9%88%d8%b1%d9%82/%d9%88%d8%b1%d9%82-%d8%b3%d8%b1%d8%af/%d9%88%d8%b1%d9%82-%d8%b1%d9%88%d8%ba%d9%86%db%8c/'
            #'rangi@https://ahanhyper.com/product-category/%d9%88%d8%b1%d9%82/%d9%88%d8%b1%d9%82-%d8%b3%d8%b1%d8%af/%d9%88%d8%b1%d9%82-%d8%b1%d9%86%da%af%db%8c/'
            #'galvanize@https://ahanhyper.com/product-category/%d9%88%d8%b1%d9%82/%d9%88%d8%b1%d9%82-%d8%b3%d8%b1%d8%af/%d9%88%d8%b1%d9%82-%da%af%d8%a7%d9%84%d9%88%d8%a7%d9%86%db%8c%d8%b2%d9%87/'
            #aliazhi
            #asid shoei
            'https://ahanhyper.com/product-category/%d9%88%d8%b1%d9%82/%d9%88%d8%b1%d9%82-%da%af%d8%b1%d9%85/%d9%88%d8%b1%d9%82-%d8%a2%d8%ac%d8%af%d8%a7%d8%b1/'
        ]
        
        for url in varagh:
            self.type = url.split("@")[1]
            yield scrapy.Request(url=url, callback=self.varagh_parser)

        for url in profil:
            self.type = url.split("@")[1]
            yield scrapy.Request(url=url, callback=self.profil_parser)

        for url in tir_ahan:
            self.type = url.split("@")[1]
            yield scrapy.Request(url=url, callback=self.tirahan_parser)

        for url in urls:
            self.type = url.split("@")[1]
            yield scrapy.Request(url=url, callback=self.parse)

    def varagh_parser(self, response):

        for res in response.css('table.ninja_footable'):
            
            for row in res.xpath('//tr'):
                if row.xpath('td[6]//text()').extract_first() == None:
                    continue

                print(requests.post(

                        url="https://apinew.samaneahan.com/api/v3/crawler/product/bulk",
                        headers={
                        'Accept': 'application/vnd.SamaneAhan.v2+json',
                        },
                        json = {
                            'data':[
                                {
                                    'category':'website',
                                    'type_id':1,
                                    'kind' : self.type,
                                    'site': 'هایپر آهن',
                                    'code' : row.xpath('td[1]//text()').extract_first(),
                                    'name': row.xpath('td[2]//text()').extract_first(),
                                    'location': row.xpath('td[3]//text()').extract_first(),
                                    'size': row.xpath('td[4]//text()').extract_first(),
                                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                                    'price' : row.xpath('td[6]//text()').extract_first(),
                                    'detail' : row.xpath('td[7]//text()').extract_first()
                                    
                                }
                            ]
                        }
                    ).status_code)

                print({
                    'code' : row.xpath('td[1]//text()').extract_first(),
                    'name': row.xpath('td[2]//text()').extract_first(),
                    'location': row.xpath('td[3]//text()').extract_first(),
                    'size': row.xpath('td[4]//text()').extract_first(),
                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                    'price' : row.xpath('td[6]//text()').extract_first(),
                    'detail' : row.xpath('td[7]//text()').extract_first()
                })
            break

    def profil_parser(self, response):

        for res in response.css('table.ninja_footable'):
            
   
            for row in res.xpath('//tr'):
                if row.xpath('td[5]//text()').extract_first() == None:
                    continue
            
                
                print(requests.post(

                        url="https://apinew.samaneahan.com/api/v3/crawler/product/bulk",
                        headers={
                        'Accept': 'application/vnd.SamaneAhan.v2+json',
                        },
                        json = {
                            'data':[
                                {
                                    'category':'website',
                                    'type_id':1,
                                    'kind' : self.type,
                                    'site': 'هایپر آهن',
                                    'code' : row.xpath('td[1]//text()').extract_first(),
                                    'name': row.xpath('td[2]//text()').extract_first(),
                                    'location': row.xpath('td[3]//text()').extract_first(),
                                    'size': row.xpath('td[4]//text()').extract_first(),
                                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                                    'weight' : row.xpath('td[6]//text()').extract_first(),
                                    'price' : row.xpath('td[7]//text()').extract_first(),
                                    'detail' : row.xpath('td[8]//text()').extract_first()
                                }
                            ]
                        }
                    ).status_code)
                
                print({
                    'code' : row.xpath('td[1]//text()').extract_first(),
                    'name': row.xpath('td[2]//text()').extract_first(),
                    'location': row.xpath('td[3]//text()').extract_first(),
                    'size': row.xpath('td[4]//text()').extract_first(),
                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                    'weight' : row.xpath('td[6]//text()').extract_first(),
                    'price' : row.xpath('td[7]//text()').extract_first(),
                    'detail' : row.xpath('td[8]//text()').extract_first()
                })
            break

    def tirahan_parser(self, response):

        for res in response.css('table.ninja_footable'):
            
            # for length in range(0,len(response.css('h2.product-title'))):
            #     print("[+]" + response.css('h2.product-title a::text')[length].get())
            for row in res.xpath('//tr'):
                if row.xpath('td[5]//text()').extract_first() == None:
                    continue

                print(requests.post(

                        url="https://apinew.samaneahan.com/api/v3/crawler/product/bulk",
                        headers={
                        'Accept': 'application/vnd.SamaneAhan.v2+json',
                        },
                        json = {
                            'data':[
                                {
                                    'category':'website',
                                    'type_id':1,
                                    'kind' : self.type,
                                    'site': 'هایپر آهن',
                                    'code' : row.xpath('td[1]//text()').extract_first(),
                                    'name': row.xpath('td[2]//text()').extract_first(),
                                    'location': row.xpath('td[3]//text()').extract_first(),
                                    'size': row.xpath('td[4]//text()').extract_first(),
                                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                                    'weight' : row.xpath('td[6]//text()').extract_first(),
                                    'price' : row.xpath('td[7]//text()').extract_first(),
                                    'detail' : row.xpath('td[8]//text()').extract_first()
                                }
                            ]
                        }
                    ).status_code)


                print({
                    'code' : row.xpath('td[1]//text()').extract_first(),
                    'name': row.xpath('td[2]//text()').extract_first(),
                    'location': row.xpath('td[3]//text()').extract_first(),
                    'size': row.xpath('td[4]//text()').extract_first(),
                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                    'weight' : row.xpath('td[6]//text()').extract_first(),
                    'price' : row.xpath('td[7]//text()').extract_first(),
                    'detail' : row.xpath('td[8]//text()').extract_first()
                })
            break
        
    def parse(self, response):

        for res in response.css('table.ninja_footable'):
            
            # for length in range(0,len(response.css('h2.product-title'))):
            #     print("[+]" + response.css('h2.product-title a::text')[length].get())
            for row in res.xpath('//tr'):
                if row.xpath('td[5]//text()').extract_first() == None:
                    continue
            
                    
                print(requests.post(

                        url="https://apinew.samaneahan.com/api/v3/crawler/product/bulk",
                        headers={
                        'Accept': 'application/vnd.SamaneAhan.v2+json',
                        },
                        json = {
                            'data':[
                                {
                                    'category':'website',
                                    'type_id':1,
                                    'kind' : self.type,
                                    'site': 'هایپر آهن',
                                    'code' : row.xpath('td[1]//text()').extract_first(),
                                    'name': row.xpath('td[2]//text()').extract_first(),
                                    'location': row.xpath('td[3]//text()').extract_first(),
                                    'length': row.xpath('td[4]//text()').extract_first(),
                                    'size': row.xpath('td[5]//text()').extract_first(),
                                    'vahed' : row.xpath('td[6]//text()').extract_first(),
                                    'weight' : row.xpath('td[7]//text()').extract_first(),
                                    'price' : row.xpath('td[8]//text()').extract_first(),
                                    'detail' : row.xpath('td[9]//text()').extract_first()
                                }
                            ]
                        }
                    ).status_code)


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