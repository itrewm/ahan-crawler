import scrapy
import json



# type_id
# تیرآهن : 1
# میلگرد : 2
# قوطی و پروفیل : 3
# ورق : 5
# نبشی : 6
# ناودانی : 7

# ورق سرد و گرم فقط داره
# در پروفیل ها : https://tehran-ahan.com/product-category/industrial-tube/ فقط گرفته شد


class AsreahanTableSpider(scrapy.Spider):

    name = 'asreahan'

    type = ""

    def start_requests(self):

        milgerd = [
            'آجدار@https://asreahan.com/product/rebar/',

        ]
        
        tir_ahan = [
            #'معمولی@https://pivan.co/product-category/beam-h/iron-girder/',
            'هاش@https://pivan.co/product-category/beam-h/h/'
            'هاش@https://pivan.co/product-category/beam-h/h/page/2/',
            'هاش@https://pivan.co/product-category/beam-h/h/page/3/',
            'هاش@https://pivan.co/product-category/beam-h/h/page/4/',
            'هاش@https://pivan.co/product-category/beam-h/h/page/5/',
            'هاش@https://pivan.co/product-category/beam-h/h/page/6/'
            # ERORRRRRR stm not run
        ]

        profil_urls = [
            'https://pivan.co/product-category/profile/industrial-profile/'
        ]

        nabshi_urls = [
            'https://pivan.co/product-category/angel/construction-angel/'
        ]

        navdani_urls = [
            'https://pivan.co/product-category/uchannel/',
            'https://pivan.co/product-category/uchannel/page/2/'
        ]

        for url in milgerd:
            splited_url = url.split("@")
            self.type = splited_url[0]
            yield scrapy.Request(url=splited_url[1], callback=self.get_compony_tag)

        # for url in tir_ahan:
        #     splited_url = url.split("@")
        #     self.type = splited_url[0]
        #     yield scrapy.Request(url=splited_url[1], callback=self.tirahan_parse)


        # for url in profil_urls:
        #     yield scrapy.Request(url=url, callback=self.profil_parse)
    
        # for url in nabshi_urls:
        #     yield scrapy.Request(url=url, callback=self.nabshi_parse)


        # for url in navdani_urls:
        #     yield scrapy.Request(url=url, callback=self.navdani_parse)




    def navdani_parse(self, response):
        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue

                print({

                    'category':'website',
                    'type_id':7,
                    'kind' : 'ناودانی',
                    'site': 'پیوان',


                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'size': row.xpath('div[2]//text()').extract_first(),
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
                    'kind' : 'نبشی',
                    'site': 'پیوان',


                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'size': row.xpath('div[2]//text()').extract_first(),
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
                    
                print({

                    'category':'website',
                    'type_id':1,
                    'kind' : self.type,
                    'site': 'پیوان',
                    'name' : row.xpath('div[1]//text()').extract_first(),
                    'zekhamat': row.xpath('div[2]//text()').extract_first(),
                    'size': row.xpath('div[3]//text()').extract_first(),
                    'weight': row.xpath('div[4]//text()').extract_first(),
                    'tahvil': row.xpath('div[5]//text()').extract_first(),
                    'vahed': row.xpath('div[6]//text()').extract_first(),
                    'price': row.xpath('div[7]//text()').extract_first()

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
                                'kind' : self.type,
                                'site': 'پیوان',
                                'name' : row.xpath('div[1]//text()').extract_first(),
                                'zekhamat': row.xpath('div[2]//text()').extract_first(),
                                'size': row.xpath('div[3]//text()').extract_first(),
                                'weight': row.xpath('div[4]//text()').extract_first(),
                                'tahvil': row.xpath('div[5]//text()').extract_first(),
                                'vahed': row.xpath('div[6]//text()').extract_first(),
                                'price': row.xpath('div[7]//text()').extract_first()
                            }
                        ]
                    }
                ).status_code)


    def tirahan_parse(self, response):

        for res in response.css('section.list'):

            for row in res.xpath('//div[re:test(@class, "^list-item")]'):

                if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
                    continue
                    
                print({

                    'category':'website',
                    'type_id':1,
                    'kind' : self.type,
                    'site': 'پیوان',


                    'name' : row.xpath('div[1]//text()').extract_first(),
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
                                'kind' : self.type,
                                'site': 'پیوان',
                                'name' : row.xpath('div[1]//text()').extract_first(),
                                'size': row.xpath('div[2]//text()').extract_first(),
                                'weight': row.xpath('div[3]//text()').extract_first(),
                                'tahvil': row.xpath('div[4]//text()').extract_first(),
                                'vahed': row.xpath('div[5]//text()').extract_first(),
                                'price': row.xpath('div[6]//text()').extract_first()
                            }
                        ]
                    }
                ).status_code)


    def get_compony_tag(self, response):

        def request_handler(response):
            
            print(json.dump(response.xpath('//script//text()').extract_first()))
            # for res in response.css('table.MuiTable-root'):

            #     for row in res.xpath('tbody//tr'):
                
            #         if row.xpath('td[1]//text()').extract_first() == None:
            #             continue
                    

            #         if row.xpath('td[4]//p//text()').extract() == []:
            #             price = "تماس بگیرید"
                    
            #         else:
            #             price = row.xpath('td[4]//p//text()').extract()

            #         print({

            #             'category':'website',
            #             'type_id':1,
            #             'kind' : self.type,
            #             'site': 'عصر آهن',


            #             'name' : row.xpath('td[1]//span[1]//text()').extract_first() + row.xpath('td[1]//span[2]//text()').extract_first(),
            #             'size': row.xpath('td[2]//text()').extract_first(),
            #             'standard': row.xpath('td[3]//text()').extract_first(),
            #             'price' : price,
            #             'weight' : row.xpath('td[5]//text()').extract_first(),
            #             'bargiri' : row.xpath('td[6]//text()').extract_first()

            #         })
            
                    
            
            



        for res in response.css('div.jss47'):
            for href in res.xpath('//a[re:test(@class, "MuiButton-outlined")]//@href'):
                #self.request_handler(href.extract())
                if href.get() == "/factories/%D8%B0%D9%88%D8%A8-%D8%A2%D9%87%D9%86-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86":
                    yield scrapy.Request(url="https://asreahan.com" + href.extract(), callback=request_handler)
            # for row in res.xpath('//div[re:test(@class, "^list-item")]'):

            #     if row.xpath('div[1]//text()').extract_first() == "عنوان کالا":
            #         continue
                    
            #     print({

            #         'category':'website',
            #         'type_id':2,
            #         'kind' : self.type,
            #         'site': 'پیوان',
            #         'name' : row.xpath('div[1]//text()').extract_first(),
            #         'length': row.xpath('div[2]//text()').extract_first(),
            #         'weight': row.xpath('div[3]//text()').extract_first(),
            #         'tahvil': row.xpath('div[4]//text()').extract_first(),
            #         'vahed': row.xpath('div[5]//text()').extract_first(),
            #         'price': row.xpath('div[6]//text()').extract_first()

            #     })
           
            #     print(requests.post(

            #         url="https://apinew.samaneahan.com/api/v3/crawler/product/bulk",
            #         headers={
            #         'Accept': 'application/vnd.SamaneAhan.v2+json',
            #         },
            #         json = {
            #             'data':[
            #                 {
            #                     'category':'website',
            #                     'type_id':2,
            #                     'kind' : self.type,
            #                     'site': 'پیوان',
            #                     'name' : row.xpath('div[1]//text()').extract_first(),
            #                     'length': row.xpath('div[2]//text()').extract_first(),
            #                     'weight': row.xpath('div[3]//text()').extract_first(),
            #                     'tahvil': row.xpath('div[4]//text()').extract_first(),
            #                     'vahed': row.xpath('div[5]//text()').extract_first(),
            #                     'price': row.xpath('div[6]//text()').extract_first()
            #                 }
            #             ]
            #         }
            #     ).status_code)


        
                

