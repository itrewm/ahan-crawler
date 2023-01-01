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


class IromartTableSpider(scrapy.Spider):

    name = 'iromart'

    type = ""

    def start_requests(self):

        milgerd = [
            'آجدار@https://iromart.com/round-bar/ribbed/',
            'ساده@https://iromart.com/round-bar/plain/'
        ]
        
        tir_ahan = [
            'معمولی@https://iromart.com/beam/',
            'هاش@https://iromart.com/beam/ipb/'
        ]

        profil_urls = [
            'https://iromart.com/profile/%d9%be%d8%b1%d9%88%d9%81%db%8c%d9%84-%d8%b5%d9%86%d8%b9%d8%aa%db%8c/'
        ]

        nabshi_urls = [
            'https://iromart.com/l-profile/'
        ]

        navdani_urls = [
            'https://iromart.com/channel/'
        ]

        for url in milgerd:
            splited_url = url.split("@")
            self.type = splited_url[0]
            yield scrapy.Request(url=splited_url[1], callback=self.milgerd_parse)


        for url in tir_ahan:
            splited_url = url.split("@")
            self.type = splited_url[0]
            yield scrapy.Request(url=splited_url[1], callback=self.tirahan_parse)


        for url in profil_urls:
            yield scrapy.Request(url=url, callback=self.profil_parse)
    

        for url in nabshi_urls:
            yield scrapy.Request(url=url, callback=self.nabshi_parse)


        for url in navdani_urls:
            yield scrapy.Request(url=url, callback=self.navdani_parse)



    def navdani_parse(self, response):
        
        for res in response.css('table.datait_184'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                

                print({

                    'category':'website',
                    'type_id':1,
                    'kind' : self.type,
                    'site': 'آیرومات',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'vahed': row.xpath('td[2]//text()').extract_first(),

                    'lenght' : row.xpath('td[3]//text()').extract_first(),
                    'jan-lenght' : row.xpath('td[4]//text()').extract_first(),
                    'brand' : row.xpath('td[5]//text()').extract_first(),
                    'bargiri' : row.xpath('td[6]//text()').extract_first(),
                    'price' : row.xpath('td[8]//div//strong//text()').extract_first()

                })


    def nabshi_parse(self, response):

        for res in response.css('table.datait_186'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                

                print({

                    'category':'website',
                    'type_id':1,
                    'kind' : self.type,
                    'site': 'آیرومات',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'vahed': row.xpath('td[2]//text()').extract_first(),
                    'size': row.xpath('td[3]//text()').extract_first(),
                    'lenght' : row.xpath('td[4]//text()').extract_first(),
                    'zekhamat' : row.xpath('td[5]//text()').extract_first(),
                    'brand' : row.xpath('td[6]//text()').extract_first(),
                    'bargiri' : row.xpath('td[7]//text()').extract_first(),
                    'price' : row.xpath('td[9]//div//strong//text()').extract_first()

                })


    def profil_parse(self, response):

        #loop = response.css('table.datait_183') if self.type == "معمولی" else response.css('table.datait_155')
        
        for res in response.css('table.datait_312_11'):

            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                

                print({

                    'category':'website',
                    'type_id':1,
                    'kind' : self.type,
                    'site': 'آیرومات',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'size': row.xpath('td[2]//text()').extract_first(),
                    'zekhamat': row.xpath('td[3]//text()').extract_first(),
                    'lenght' : row.xpath('td[4]//text()').extract_first(),
                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                    'bargiri' : row.xpath('td[6]//text()').extract_first(),
                    'city' : row.xpath('td[7]//text()').extract_first(),
                    'price' : row.xpath('td[8]//div//strong//text()').extract_first()

                })
                    
             
                    
                    # print({

                    #     'category':'website',
                    #     'type_id':1,
                    #     'kind' : self.type,
                    #     'site': 'آیرومات',

                    #     'name' : row.xpath('td[1]//span//text()').extract_first(),
                    #     'vahed': row.xpath('td[2]//text()').extract_first(),
                    #     'standard': row.xpath('td[3]//text()').extract_first(),
                    #     'size' : row.xpath('td[4]//text()').extract_first(),
                    #     'lenght' : row.xpath('td[5]//text()').extract_first(),
                    #     'weight' : row.xpath('td[6]//text()').extract_first(),
                    #     'brand' : row.xpath('td[7]//text()').extract_first(),
                    #     'bargiri' : row.xpath('td[8]//text()').extract_first(),
                    #     'price' : row.xpath('td[10]//div//strong//text()').extract_first(),

                    # })


    def tirahan_parse(self, response):
        
        loop = response.css('table.datait_183') if self.type == "معمولی" else response.css('table.datait_155')
        
        for res in loop:
            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                
                if self.type == "معمولی":
                    print({

                        'category':'website',
                        'type_id':1,
                        'kind' : self.type,
                        'site': 'آیرومات',

                        'name' : row.xpath('td[1]//span//text()').extract_first(),
                        'vahed': row.xpath('td[2]//text()').extract_first(),
                        'size': row.xpath('td[3]//text()').extract_first(),
                        'lenght' : row.xpath('td[4]//text()').extract_first(),
                        'brand' : row.xpath('td[5]//text()').extract_first(),
                        'bargiri' : row.xpath('td[6]//text()').extract_first(),
                        'price' : row.xpath('td[8]//div//strong//text()').extract_first()

                    })
                    
                elif self.type == "هاش":
                    
                    print({

                        'category':'website',
                        'type_id':1,
                        'kind' : self.type,
                        'site': 'آیرومات',

                        'name' : row.xpath('td[1]//span//text()').extract_first(),
                        'vahed': row.xpath('td[2]//text()').extract_first(),
                        'standard': row.xpath('td[3]//text()').extract_first(),
                        'size' : row.xpath('td[4]//text()').extract_first(),
                        'lenght' : row.xpath('td[5]//text()').extract_first(),
                        'weight' : row.xpath('td[6]//text()').extract_first(),
                        'brand' : row.xpath('td[7]//text()').extract_first(),
                        'bargiri' : row.xpath('td[8]//text()').extract_first(),
                        'price' : row.xpath('td[10]//div//strong//text()').extract_first(),

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

        loop = response.css('table.datait_123') if self.type == "آجدار" else response.css('table.datait_124')


        for res in loop:
            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//span//text()').extract_first() == None:
                    continue
                    
                print({

                    'category':'website',
                    'type_id':2,
                    'kind' : self.type,
                    'site': 'آیرومات',

                    'name' : row.xpath('td[1]//span//text()').extract_first(),
                    'vahed': row.xpath('td[2]//text()').extract_first(),
                    'size': row.xpath('td[3]//text()').extract_first(),
                    'halat' : row.xpath('td[4]//text()').extract_first(),
                    'standard' : row.xpath('td[5]//text()').extract_first(),
                    'bargiri' : row.xpath('td[6]//text()').extract_first(),
                    'brand' : row.xpath('td[7]//text()').extract_first(),
                    'price' : row.xpath('td[9]//div//strong//text()').extract_first()

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


        
                

