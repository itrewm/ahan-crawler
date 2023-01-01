import scrapy

# type_id
# تیرآهن : 1
# میلگرد : 2
# قوطی و پروفیل : 3
# ورق : 5
# نبشی : 6
# ناودانی : 7

# ورق سرد و گرم فقط داره
# در پروفیل ها : https://tehran-ahan.com/product-category/industrial-tube/ فقط گرفته شد


class FooladTableSpider(scrapy.Spider):

    name = 'fooladiranian'

    type = ""

    def start_requests(self):

        milgerd = [
            'آجدار@https://www.fooladiranian.com/productlist/%D9%85%DB%8C%D9%84%DA%AF%D8%B1%D8%AF-%D8%A2%D8%AC%D8%AF%D8%A7%D8%B1/',
            'ساده@https://www.fooladiranian.com/productlist/%D9%85%DB%8C%D9%84%DA%AF%D8%B1%D8%AF-%D8%B3%D8%A7%D8%AF%D9%87/'
        ]
        
        tir_ahan = [
            'معمولی@https://www.fooladiranian.com/productlist/%D8%AA%DB%8C%D8%B1%D8%A2%D9%87%D9%86/',
            'هاش@https://www.fooladiranian.com/productlist/%D8%AA%DB%8C%D8%B1%D8%A2%D9%87%D9%86-%D9%87%D8%A7%D8%B4/'
        ]

        profil_urls = [
            'https://www.fooladiranian.com/productlist/%D9%BE%D8%B1%D9%88%D9%81%DB%8C%D9%84-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C/'
        ]

        nabshi_urls = [
            'https://www.fooladiranian.com/productlist/%D9%86%D8%A8%D8%B4%DB%8C/'
        ]

        navdani_urls = [
            'https://www.fooladiranian.com/productlist/%D9%86%D8%A7%D9%88%D8%AF%D8%A7%D9%86%DB%8C/'
        ]

        # for url in milgerd:
        #     splited_url = url.split("@")
        #     self.type = splited_url[0]
        #     yield scrapy.Request(url=splited_url[1], callback=self.milgerd_parse)


        # for url in tir_ahan:
        #     splited_url = url.split("@")
        #     self.type = splited_url[0]
        #     yield scrapy.Request(url=splited_url[1], callback=self.tirahan_parse)


        # for url in profil_urls:
        #     yield scrapy.Request(url=url, callback=self.profil_parse)
    

        # for url in nabshi_urls:
        #     yield scrapy.Request(url=url, callback=self.nabshi_parse)


        for url in navdani_urls:
            yield scrapy.Request(url=url, callback=self.navdani_parse)



    def navdani_parse(self, response):
        
        for res in response.css('table.TableList_container__1HOjj'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                
                
                print({

                    'category':'website',
                    'type_id':2,
                    'kind' : self.type,
                    'site': 'فولاد ایرانیان',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'size': row.xpath('td[2]//text()').extract_first(),
                    'lenght': row.xpath('td[3]//text()').extract_first(),
                    'tahvil' : row.xpath('td[4]//text()').extract_first(),
                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                    'price' : row.xpath('td[6]//text()').extract_first(),
   

                })


    def nabshi_parse(self, response):

        for res in response.css('table.TableList_container__1HOjj'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                
                
                print({

                    'category':'website',
                    'type_id':2,
                    'kind' : self.type,
                    'site': 'فولاد ایرانیان',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'size': row.xpath('td[2]//text()').extract_first(),
                    'lenght': row.xpath('td[3]//text()').extract_first(),
                    'zekhamat' : row.xpath('td[4]//text()').extract_first(),
                    'tahvil' : row.xpath('td[5]//text()').extract_first(),
                    'vahed' : row.xpath('td[6]//text()').extract_first(),
                    'price' : row.xpath('td[7]//text()').extract_first()

                })


    def profil_parse(self, response):

        for res in response.css('table.TableList_container__1HOjj'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                
                
                print({

                    'category':'website',
                    'type_id':2,
                    'kind' : self.type,
                    'site': 'فولاد ایرانیان',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'zekhamat': row.xpath('td[2]//text()').extract_first(),
                    'tahvil': row.xpath('td[3]//text()').extract_first(),
                    'vahed' : row.xpath('td[4]//text()').extract_first(),
                    'lenght' : row.xpath('td[5]//text()').extract_first(),
                    'price' : row.xpath('td[6]//text()').extract_first()

                })


    def tirahan_parse(self, response):
        
        for res in response.css('table.TableList_container__1HOjj'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                
                if self.type == "معمولی":
                    print({

                        'category':'website',
                        'type_id':2,
                        'kind' : self.type,
                        'site': 'فولاد ایرانیان',

                        'name' : row.xpath('td[1]//span//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'standard': row.xpath('td[3]//text()').extract_first(),
                        'lenght' : row.xpath('td[4]//text()').extract_first(),
                        'weight' : row.xpath('td[5]//text()').extract_first(),
                        'tahvil' : row.xpath('td[6]//text()').extract_first(),
                        'vahed' : row.xpath('td[7]//text()').extract_first(),
                        'price' : row.xpath('td[8]//text()').extract_first()

                    })

                elif self.type == "هاش":

                    print({

                        'category':'website',
                        'type_id':2,
                        'kind' : self.type,
                        'site': 'فولاد ایرانیان',

                        'name' : row.xpath('td[1]//span//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'standard': row.xpath('td[3]//text()').extract_first(),
                        'lenght' : row.xpath('td[4]//text()').extract_first(),
                        'tahvil' : row.xpath('td[5]//text()').extract_first(),
                        'vahed' : row.xpath('td[6]//text()').extract_first(),
                        'price' : row.xpath('td[7]//text()').extract_first()

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
                #                 'type_id':2,
                #                 'kind' : self.type,
                #                 'site': 'پیوان',

                #                 'name' : row.xpath('td[1]//span//text()').extract_first(),
                #                 'vahed': row.xpath('td[2]//text()').extract_first(),
                #                 'size': row.xpath('td[3]//text()').extract_first(),
                #                 'halat' : row.xpath('td[4]//text()').extract_first(),
                #                 'standard' : row.xpath('td[5]//text()').extract_first(),
                #                 'bargiri' : row.xpath('td[6]//text()').extract_first(),
                #                 'brand' : row.xpath('td[7]//text()').extract_first(),
                #                 'price' : row.xpath('td[9]//div//strong//text()').extract_first()
                #             }
                #         ]
                #     }
                # ).status_code)



    def milgerd_parse(self, response):

    
        for res in response.css('table.TableList_container__1HOjj'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                
                if self.type == "آجدار":
                    print({

                        'category':'website',
                        'type_id':2,
                        'kind' : self.type,
                        'site': 'فولاد ایرانیان',

                        'name' : row.xpath('td[1]//span//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'standard': row.xpath('td[3]//text()').extract_first(),
                        'lenght' : row.xpath('td[4]//text()').extract_first(),
                        'weight' : row.xpath('td[5]//text()').extract_first(),
                        'tahvil' : row.xpath('td[6]//text()').extract_first(),
                        'vahed' : row.xpath('td[7]//text()').extract_first(),
                        'price' : row.xpath('td[8]//text()').extract_first()

                    })

                elif self.type == "ساده":

                    print({

                        'category':'website',
                        'type_id':2,
                        'kind' : self.type,
                        'site': 'فولاد ایرانیان',

                        'name' : row.xpath('td[1]//span//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'standard': row.xpath('td[3]//text()').extract_first(),
                        'halat' : row.xpath('td[4]//text()').extract_first(),
                        'tahvil' : row.xpath('td[5]//text()').extract_first(),
                        'vahed' : row.xpath('td[6]//text()').extract_first(),
                        'price' : row.xpath('td[7]//text()').extract_first()

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
                #                 'type_id':2,
                #                 'kind' : self.type,
                #                 'site': 'پیوان',

                #                 'name' : row.xpath('td[1]//span//text()').extract_first(),
                #                 'vahed': row.xpath('td[2]//text()').extract_first(),
                #                 'size': row.xpath('td[3]//text()').extract_first(),
                #                 'halat' : row.xpath('td[4]//text()').extract_first(),
                #                 'standard' : row.xpath('td[5]//text()').extract_first(),
                #                 'bargiri' : row.xpath('td[6]//text()').extract_first(),
                #                 'brand' : row.xpath('td[7]//text()').extract_first(),
                #                 'price' : row.xpath('td[9]//div//strong//text()').extract_first()
                #             }
                #         ]
                #     }
                # ).status_code)


        
                

