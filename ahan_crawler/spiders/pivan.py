import scrapy
import requests
from urllib.parse import urlencode
from scrapyd_api import ScrapydAPI


# type_id
# تیرآهن : 1
# میلگرد : 2
# قوطی و پروفیل : 3
# ورق : 5
# نبشی : 6
# ناودانی : 7


# ورق سرد و گرم فقط داره
# در پروفیل ها : https://tehran-ahan.com/product-category/industrial-tube/ فقط گرفته شد

API_KEY = '6ef14ac6-455f-4776-b19a-8488acd290b7'

def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class PivanTableSpider(scrapy.Spider):

    name = 'pivan'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['https://aradahan.com/product-category/milgerd']
    type = ""

    def start_requests(self):

        milgerd = [
            'آجدار@https://pivan.co/product-category/rebar/ribbed-rebar/',
            'آجدار@https://pivan.co/product-category/rebar/ribbed-rebar/page/2/',
            'ساده@https://pivan.co/product-category/rebar/simple-rebar/',
            'ساده@https://pivan.co/product-category/rebar/simple-rebar/page/2/'
        ]
        
        tir_ahan = [
            'https://pivan.co/product-category/beam-h/iron-girder/',
            'https://pivan.co/product-category/beam-h/h/'
            'https://pivan.co/product-category/beam-h/h/page/2/',
            'https://pivan.co/product-category/beam-h/h/page/3/',
            'https://pivan.co/product-category/beam-h/h/page/4/',
            'https://pivan.co/product-category/beam-h/h/page/5/',
            # ERORRRRRR stm not run
        ]

        profil_urls = [
            'https://pivan.co/product-category/profile/industrial-profile/',
            'https://pivan.co/product-category/profile/building-profile/'
        ]

        nabshi_urls = [
            'https://pivan.co/product-category/angel/construction-angel/',
            'https://pivan.co/product-category/angel/construction-angel/page/2/'
        ]

        navdani_urls = [
            'https://pivan.co/product-category/uchannel/',
            'https://pivan.co/product-category/uchannel/page/2/'
        ]

        # for url in milgerd:
        #     splited_url = url.split("@")
        #     self.type = splited_url[0]
        #     yield scrapy.Request(url=splited_url[1], callback=self.milgerd_parse)

        # for url in tir_ahan:
        #     yield scrapy.Request(url=url, callback=self.tirahan_parse)


        # for url in profil_urls:
        #     yield scrapy.Request(url=url, callback=self.profil_parse)
    
        # for url in nabshi_urls:
        #     yield scrapy.Request(url=url, callback=self.nabshi_parse)


        for url in navdani_urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.navdani_parse)



    def navdani_parse(self, response):
        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue

                print({

                    'category':'website',
                    'type_id':7,
                    'kind' : 'ناودانی',
                    'site': 'https://pivan.co/',


                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'size': row.xpath('div[2]//text()').extract_first(),
                    'company': row.xpath('div[1]//text()').extract_first().split("-")[2].replace(" ",""), 
                    'weight': row.xpath('div[3]//text()').extract_first(),
                    'tahvil': row.xpath('div[4]//text()').extract_first(),
                    'vahed': row.xpath('div[5]//text()').extract_first(),
                    'price': row.xpath('div[6]//text()').extract_first()
                })


    def nabshi_parse(self, response):

        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue

                print({

                    'category':'website',
                    'type_id':6,
                    'kind' : 'نبشی ساختمانی',
                    'site': 'https://pivan.co/',

                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'size': row.xpath('div[2]//text()').extract_first(),
                    'company': row.xpath('div[1]//text()').extract_first().split("-")[2].replace(" ",""), 
                    'zekhamat': row.xpath('div[3]//text()').extract_first(),
                    'weight': row.xpath('div[4]//text()').extract_first(),
                    'tahvil': row.xpath('div[5]//text()').extract_first(),
                    'vahed': row.xpath('div[6]//text()').extract_first(),
                    'price': row.xpath('div[7]//text()').extract_first()
                })


    def profil_parse(self, response):

        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue


                p_type = "صنعتی" if "صنعتی" in response.xpath("//h2//a//text()").extract_first() else "ساختمانی"
                   
                
                print({

                    'category':'website',
                    'type_id':3,
                    'kind' : p_type,

                    'site': 'https://pivan.co/',
                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'zekhamat': row.xpath('div[2]//text()').extract_first(),
                    'company':row.xpath('div[1]//text()').extract_first().split("-")[2].replace(" ",""),
                    'size': row.xpath('div[3]//text()').extract_first(),
                    'weight': row.xpath('div[4]//text()').extract_first(),
                    'tahvil':row.xpath('div[5]//text()').extract_first() ,
                    'vahed': row.xpath('div[6]//text()').extract_first(),
                    'price': row.xpath('div[7]//text()').extract_first()

                })

                
                # print(requests.post(

                #     url="https://apinew.samaneahan.com/api/v3/crawler/product/bulk",
                #     headers={
                #     'Accept': 'application/vnd.SamaneAhan.v2+json',
                #     },
                #     json = {
                #         'data':[
                #             {
                #                 'category':'website',
                #                 'type_id':3,
                #                 'kind' : self.type,
                #                 'site': 'https://pivan.co/',
                #                 'name' : row.xpath('div[1]//text()').extract_first(),
                #                 'zekhamat': row.xpath('div[2]//text()').extract_first(),
                #                 'size': row.xpath('div[3]//text()').extract_first(),
                #                 'weight': row.xpath('div[4]//text()').extract_first(),
                #                 'tahvil': row.xpath('div[5]//text()').extract_first(),
                #                 'vahed': row.xpath('div[6]//text()').extract_first(),
                #                 'price': row.xpath('div[7]//text()').extract_first()
                #             }
                #         ]
                #     }
                # ).status_code)


    def tirahan_parse(self, response):

        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue

                if "هاش" in row.xpath('div[1]//text()').extract_first():
                    p_type = "هاش"
                    company = row.xpath('div[1]//text()').extract_first().split("-")[3].replace(" ","")

                else:
                    p_type = "معمولی"
                    company = row.xpath('div[1]//text()').extract_first().split("-")[1].replace(" ","")



                print({

                    'category':'website',
                    'type_id':1,
                    'kind' : p_type,
                    'site': 'https://pivan.co/',
                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'compay' : company,
                    'size': row.xpath('div[2]//text()').extract_first(),
                    'weight': row.xpath('div[3]//text()').extract_first(),
                    'tahvil': row.xpath('div[4]//text()').extract_first(),
                    'vahed': row.xpath('div[5]//text()').extract_first(),
                    'price': row.xpath('div[6]//text()').extract_first()

                })

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
                                'kind' : p_type,
                                'site': 'https://pivan.co/',
                                'name' : row.xpath('div[1]//text()').extract_first(),
                                'compay' : company,
                                'size': row.xpath('div[2]//text()').extract_first(),
                                'weight': row.xpath('div[3]//text()').extract_first(),
                                'tahvil': row.xpath('div[4]//text()').extract_first(),
                                'vahed': row.xpath('div[5]//text()').extract_first(),
                                'price': row.xpath('div[6]//text()').extract_first()
                            }
                        ]
                    }
                ).status_code)


            break

    def milgerd_parse(self, response):

        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue

                
                if "ساده" in row.xpath('div[1]//text()').extract_first():
                    p_type = "ساده"
                    compony = row.xpath('div[1]//text()').extract_first().split("-")[1].replace(" ","")

                else:
                    p_type = "آجدار"
                    compony = row.xpath('div[1]//text()').extract_first().split("-")[2].replace(" ","")

                
                
                print({

                    'category':'website',
                    'type_id':2,
                    'kind' : p_type,
                    'site': 'https://pivan.co/',
                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'compony' : compony,
                    'length': row.xpath('div[2]//text()').extract_first(),
                    'weight': row.xpath('div[3]//text()').extract_first(),
                    'tahvil': row.xpath('div[4]//text()').extract_first(),
                    'vahed': row.xpath('div[5]//text()').extract_first(),
                    'price': row.xpath('div[6]//text()').extract_first()

                })
                
                print(requests.post(

                    url="https://webhook.site/cbf317a3-8015-42fc-9e44-f58032b85a0d",
                    headers={
                    'Accept': 'application/vnd.SamaneAhan.v2+json',
                    },
                    json = {
                        'data':[
                            {
                                'category':'website',
                                'type_id':2,
                                'kind' : p_type,
                                'site': 'https://pivan.co/',
                                'name' : row.xpath('div[1]//text()').extract_first(),
                                'compony' : compony,
                                'length': row.xpath('div[2]//text()').extract_first(),
                                'weight': row.xpath('div[3]//text()').extract_first(),
                                'tahvil': row.xpath('div[4]//text()').extract_first(),
                                'vahed': row.xpath('div[5]//text()').extract_first(),
                                'price': row.xpath('div[6]//text()').extract_first()
                            }
                        ]
                    }
                ).status_code)
            
            break

        
                

