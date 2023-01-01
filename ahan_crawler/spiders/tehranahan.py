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


class TehranAhanTableSpider(scrapy.Spider):

    name = 'tehranahan'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['https://aradahan.com/product-category/milgerd']
    type = ""

    def start_requests(self):

        milgerd = [
            'آجدار@https://tehran-ahan.com/product-category/ribbed-round-bar/',
            'ساده@https://tehran-ahan.com/product-category/simple-round-bar/'
        ]
        
        tir_ahan = [
            'معمولی@https://tehran-ahan.com/product-category/beams/'
        ]

        profil_urls = [
            'https://tehran-ahan.com/product-category/industrial-tube/'
        ]

        nabshi_urls = [
            'https://tehran-ahan.com/product-category/angel'
        ]

        navdani_urls = [
            'https://tehran-ahan.com/product-category/channel/'
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

        for res in response.css('table.table-products'):
            for row in res.xpath('tbody//tr'):

                if row.xpath('td[1]//text()').extract_first() == None:
                    continue
                

                if ":" in row.xpath('td[8]//text()').extract_first():
                    print({
                        'category':'website',
                        'type_id':6,
                        'kind' : 'نبشی',
                        'site': 'تهران آهن',

                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'karkhane': row.xpath('td[3]//text()').extract_first(),
                        'lenght': row.xpath('td[4]//text()').extract_first(),
                        'vahed' : row.xpath('td[5]//text()').extract_first(),
                        'bargiri' : row.xpath('td[6]//text()').extract_first(),
                        'price' : row.xpath('td[7]//text()').extract_first()
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
                                        'type_id':6,
                                        'kind' : 'نبشی',
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'karkhane': row.xpath('td[3]//text()').extract_first(),
                                        'lenght': row.xpath('td[4]//text()').extract_first(),
                                        'vahed' : row.xpath('td[5]//text()').extract_first(),
                                        'bargiri' : row.xpath('td[6]//text()').extract_first(),
                                        'price' : row.xpath('td[7]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)



                else:
                    if "یزد" in row.xpath('td[1]//text()').extract_first():
                       
                        print({

                            'category':'website',
                            'type_id':6,
                            'kind' : 'نبشی',
                            'site': 'تهران آهن',

                            'name' : row.xpath('td[1]//text()').extract_first(),
                            'size': row.xpath('td[2]//text()').extract_first(),
                            'karkhane': row.xpath('td[3]//text()').extract_first(),
                            'lenght': row.xpath('td[4]//text()').extract_first(),
                            'bargiri' : row.xpath('td[5]//text()').extract_first(),
                            'price' : row.xpath('td[6]//text()').extract_first()
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
                                        'type_id':6,
                                        'kind' : 'نبشی',
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'karkhane': row.xpath('td[3]//text()').extract_first(),
                                        'lenght': row.xpath('td[4]//text()').extract_first(),
                                        'bargiri' : row.xpath('td[5]//text()').extract_first(),
                                        'price' : row.xpath('td[6]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)


                    else:
                    
                        
                        print({

                        'category':'website',
                        'type_id':6,
                        'kind' : 'نبشی',
                        'site': 'تهران آهن',

                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'halat': row.xpath('td[3]//text()').extract_first(),
                        'bargiri': row.xpath('td[4]//text()').extract_first(),
                        'vahed' : row.xpath('td[5]//text()').extract_first(),
                        'price' : row.xpath('td[6]//text()').extract_first()
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
                                    'type_id':6,
                                    'kind' : 'نبشی',
                                    'site': 'تهران آهن',

                                    'name' : row.xpath('td[1]//text()').extract_first(),
                                    'size': row.xpath('td[2]//text()').extract_first(),
                                    'halat': row.xpath('td[3]//text()').extract_first(),
                                    'bargiri': row.xpath('td[4]//text()').extract_first(),
                                    'vahed' : row.xpath('td[5]//text()').extract_first(),
                                    'price' : row.xpath('td[6]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)




    def nabshi_parse(self, response):

        for res in response.css('table.table-products'):
            for row in res.xpath('tbody//tr'):
                if row.xpath('td[1]//text()').extract_first() == None:
                    continue

                print({

                    'category':'website',
                    'type_id':6,
                    'kind' : 'نبشی',
                    'site': 'تهران آهن',

                    'name' : row.xpath('td[1]//text()').extract_first(),
                    'size': row.xpath('td[2]//text()').extract_first(),
                    'zekhamat': row.xpath('td[3]//text()').extract_first(),
                    'karkhane': row.xpath('td[4]//text()').extract_first(),
                    'lenght': row.xpath('td[5]//text()').extract_first(),
                    'vahed' : row.xpath('td[6]//text()').extract_first(),
                    'price' : row.xpath('td[8]//text()').extract_first()
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
                                        'type_id':6,
                                        'kind' : 'نبشی',
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'zekhamat': row.xpath('td[3]//text()').extract_first(),
                                        'karkhane': row.xpath('td[4]//text()').extract_first(),
                                        'lenght': row.xpath('td[5]//text()').extract_first(),
                                        'vahed' : row.xpath('td[6]//text()').extract_first(),
                                        'price' : row.xpath('td[8]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)


    def profil_parse(self, response):

        for res in response.css('table.table-products'):
            for row in res.xpath('tbody//tr'):


                if row.xpath('td[1]//text()').extract_first() == None:
                    continue
                

                if row.xpath('td[2]//text()').extract_first() != None and "*" in row.xpath('td[2]//text()').extract_first():
                    print({

                        'category':'website',
                        'type_id':3,
                        'kind' : self.type,
                        'site': 'تهران آهن',

                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'zekhamat': row.xpath('td[3]//text()').extract_first(),
                        'lenght': row.xpath('td[4]//text()').extract_first(),
                        'vahed': row.xpath('td[5]//text()').extract_first(),
                        'bargiti' : row.xpath('td[6]//text()').extract_first(),
                        'price' : row.xpath('td[7]//text()').extract_first(),
   
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
                                        'type_id':3,
                                        'kind' : self.type,
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'zekhamat': row.xpath('td[3]//text()').extract_first(),
                                        'lenght': row.xpath('td[4]//text()').extract_first(),
                                        'vahed': row.xpath('td[5]//text()').extract_first(),
                                        'bargiti' : row.xpath('td[6]//text()').extract_first(),
                                        'price' : row.xpath('td[7]//text()').extract_first(),
                                    }
                                ]
                            }
                        ).status_code)


                else :

                        

                    if row.xpath('td[9]//text()').extract_first() == None and row.xpath('td[8]//text()').extract_first() !=None:


                        print({

                            'category':'website',
                            'type_id':3,
                            'kind' : self.type,
                            'site': 'تهران آهن',

                            'name' : row.xpath('td[1]//text()').extract_first(),
                            'length': row.xpath('td[2]//text()').extract_first(),
                            'karkhane' : row.xpath('td[3]//text()').extract_first(),
                            'bargiri': row.xpath('td[4]//text()').extract_first(),
                            'vahed': row.xpath('td[5]//text()').extract_first(),
                            'price' : row.xpath('td[6]//text()').extract_first(),
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
                                        'type_id':3,
                                        'kind' : self.type,
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'length': row.xpath('td[2]//text()').extract_first(),
                                        'karkhane' : row.xpath('td[3]//text()').extract_first(),
                                        'bargiri': row.xpath('td[4]//text()').extract_first(),
                                        'vahed': row.xpath('td[5]//text()').extract_first(),
                                        'price' : row.xpath('td[6]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)



                    else:

                        print({

                            'category':'website',
                            'type_id':3,
                            'kind' : self.type,
                            'site': 'تهران آهن',

                            'name' : row.xpath('td[1]//text()').extract_first(),
                            'length': row.xpath('td[2]//text()').extract_first(),
                            'bargiri': row.xpath('td[3]//text()').extract_first(),
                            'vahed': row.xpath('td[4]//text()').extract_first(),
                            'price' : row.xpath('td[5]//text()').extract_first(),
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
                                        'type_id':3,
                                        'kind' : self.type,
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'length': row.xpath('td[2]//text()').extract_first(),
                                        'bargiri': row.xpath('td[3]//text()').extract_first(),
                                        'vahed': row.xpath('td[4]//text()').extract_first(),
                                        'price' : row.xpath('td[5]//text()').extract_first(),
                                    }
                                ]
                            }
                        ).status_code)


    def tirahan_parse(self, response):

        for res in response.css('table.table-products'):
            for row in res.xpath('tbody//tr'):


                if row.xpath('td[1]//text()').extract_first() == None:
                    continue


                if "هاش" in row.xpath('td[1]//text()').extract_first():

                    print({

                        'category':'website',
                        'type_id':1,    
                        'kind' : 'هاش',
                        'site': 'تهران آهن',

                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'standard': row.xpath('td[3]//text()').extract_first(),
                        'length': row.xpath('td[4]//text()').extract_first(),
                        'bargiri': row.xpath('td[5]//text()').extract_first(),
                        'price' : row.xpath('td[6]//text()').extract_first()
                   
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
                                        'kind' : 'هاش',
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'standard': row.xpath('td[3]//text()').extract_first(),
                                        'length': row.xpath('td[4]//text()').extract_first(),
                                        'bargiri': row.xpath('td[5]//text()').extract_first(),
                                        'price' : row.xpath('td[6]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)



                elif "اهواز" in row.xpath('td[1]//text()').extract_first():

                    print({

                        'category':'website',
                        'type_id':1,    
                        'kind' : 'معمولی',
                        'site': 'تهران آهن',
                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'price' : row.xpath('td[2]//text()').extract_first()
                   
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
                                        'kind' : 'معمولی',
                                        'site': 'تهران آهن',
                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'price' : row.xpath('td[2]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)

 
                else :
                    print({

                        'category':'website',
                        'type_id':1,    
                        'kind' : 'معمولی',
                        'site': 'تهران آهن',

                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'length': row.xpath('td[3]//text()').extract_first(),
                        'vahed': row.xpath('td[4]//text()').extract_first(),
                        'weight': row.xpath('td[5]//text()').extract_first(),
                        'bargiri' : row.xpath('td[6]//text()').extract_first(),
                        'price' : row.xpath('td[7]//text()').extract_first(),
                    
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
                                        'kind' : 'معمولی',
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'length': row.xpath('td[3]//text()').extract_first(),
                                        'vahed': row.xpath('td[4]//text()').extract_first(),
                                        'weight': row.xpath('td[5]//text()').extract_first(),
                                        'bargiri' : row.xpath('td[6]//text()').extract_first(),
                                        'price' : row.xpath('td[7]//text()').extract_first()
                                    }
                                ]
                            }
                        ).status_code)



    def milgerd_parse(self, response):

        for res in response.css('table.table-products'):
            for row in res.xpath('tbody//tr'):


                if row.xpath('td[1]//text()').extract_first() == None:
                    continue


                print({

                    'category':'website',
                    'type_id':2,
                    'kind' : self.type,
                    'site': 'تهران آهن',

                    'name' : row.xpath('td[1]//text()').extract_first(),
                    'size': row.xpath('td[2]//text()').extract_first(),
                    'length': row.xpath('td[3]//text()').extract_first(),
                    'standard': row.xpath('td[4]//text()').extract_first(),
                    'vahed': row.xpath('td[5]//text()').extract_first(),
                    'sort' : row.xpath('td[6]//text()').extract_first(),
                    'karkhane' : row.xpath('td[7]//text()').extract_first(),
                    'bargiri' : row.xpath('td[8]//text()').extract_first(),
                    'price' : row.xpath('td[9]//text()').extract_first(),
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
                                        'type_id':2,
                                        'kind' : self.type,
                                        'site': 'تهران آهن',

                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'length': row.xpath('td[3]//text()').extract_first(),
                                        'standard': row.xpath('td[4]//text()').extract_first(),
                                        'vahed': row.xpath('td[5]//text()').extract_first(),
                                        'sort' : row.xpath('td[6]//text()').extract_first(),
                                        'karkhane' : row.xpath('td[7]//text()').extract_first(),
                                        'bargiri' : row.xpath('td[8]//text()').extract_first(),
                                        'price' : row.xpath('td[9]//text()').extract_first(),
                                    }
                                ]
                            }
                        ).status_code)

