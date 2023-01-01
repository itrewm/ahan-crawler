import scrapy, requests, time
import re
import json 


class AradAhanTableSpider(scrapy.Spider):

    name = 'aradahan'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['https://aradahan.com/product-category/milgerd']
    tirahan_type = ""
    milgerd_type = ""

    def start_requests(self):
        
        tir_ahan = [

            # Hash sabok
            #'hash@https://aradahan.com/product-category/tirahan_-%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86/%d9%82%db%8c%d9%85%d8%aa-%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86-%d9%87%d8%a7%d8%b4-%d8%b3%d8%a8%da%a9',
            # hash sangin
            #'hashsangin@https://aradahan.com/product-category/tirahan_-%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86/%d9%82%db%8c%d9%85%d8%aa-%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86-%d9%87%d8%a7%d8%b4-%d8%b3%d9%86%da%af%db%8c%d9%86-heb'
            # Tir ahan IPE
            'ipe@https://aradahan.com/product-category/tirahan_-%d8%aa%db%8c%d8%b1%d8%a2%d9%87%d9%86/%d8%aa%db%8c%d8%b1-%d8%a2%d9%87%d9%86-ipe'
        ]

        milgerd = [
            'ajdar@https://aradahan.com/product-category/milgerd'
        ]

        # for url in tir_ahan:
        #     url_splited = url.split("@")
        #     self.tirahan_type = url_splited[0]
        #     yield scrapy.Request(url=url_splited[1], callback=self.tir_ahan_parse)
        

        for url in milgerd:
            url_splited = url.split("@")
            self.milgerd_type = url_splited[0]
            yield scrapy.Request(url=url_splited[1], callback=self.milgerd_parse)


    def tir_ahan_parse(self, response):

        for res in response.css('table.tablepress'):

            for row in res.xpath('//tr'):
                
                if row.xpath('td[1]//text()').extract_first() == None:
                    continue

                if 'hash' in self.tirahan_type :

                    if "sangin" in self.tirahan_type:
                        kind = "هاش سنگین"
                    else:
                        kind = "هاش سبک"

                    print("------------------------------------------")
                    print({
                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'size': row.xpath('td[2]//text()').extract_first(),
                        'weight': row.xpath('td[3]//text()').extract_first(),
                        'lenght' : row.xpath('td[4]//text()').extract_first(),
                        'kind' : kind,
                        'site': 'آراد آهن',
                        'price' : row.xpath('td[5]//text()').extract_first()
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
                                    'name': row.xpath('td[1]//text()').extract_first(),
                                    'size': row.xpath('td[2]//text()').extract_first(),
                                    'weight': row.xpath('td[3]//text()').extract_first(),
                                    'lenght' : row.xpath('td[4]//text()').extract_first(),
                                    'kind' : 'هاش سبک',
                                    'site': 'آراد آهن',
                                    'price' : row.xpath('td[5]//text()').extract_first()
                                }
                            ]
                        }
                    ).status_code)
                
                elif self.tirahan_type == 'ipe':
                    
                    if len(row.xpath('td[3]//text()').extract_first()) < 3 and row.xpath('td[3]//text()').extract_first() != "-":
                        
                        
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
                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'length': row.xpath('td[3]//text()').extract_first(),
                                        'weight' : row.xpath('td[4]//text()').extract_first(),
                                        'price' : row.xpath('td[6]//text()').extract_first(),
                                        'kind' : 'معمولی',
                                        'site': 'آراد آهن'
                                    }
                                ]
                            }
                        ).status_code)

                        print({
                            'name' : row.xpath('td[1]//text()').extract_first(),
                            'size': row.xpath('td[2]//text()').extract_first(),
                            'length': row.xpath('td[3]//text()').extract_first(),
                            'weight' : row.xpath('td[4]//text()').extract_first(),
                            'price' : row.xpath('td[6]//text()').extract_first()
                        })
                    

                    else:
                        
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
                                        'name' : row.xpath('td[1]//text()').extract_first(),
                                        'size': row.xpath('td[2]//text()').extract_first(),
                                        'weight': row.xpath('td[3]//text()').extract_first(),
                                        'price' : row.xpath('td[7]//text()').extract_first(),
                                        'kind' : 'معمولی',
                                        'site': 'آراد آهن'
                                    }
                                ]
                            }
                        ).status_code)

                
                        print({
                            'name' : row.xpath('td[1]//text()').extract_first(),
                            'size': row.xpath('td[2]//text()').extract_first(),
                            'weight': row.xpath('td[3]//text()').extract_first(),
                            'price' : row.xpath('td[7]//text()').extract_first()
                        })


                # print({
                #     'name' : row.xpath('td[1]//text()').extract_first(),
                #     'analyse': row.xpath('td[2]//text()').extract_first(),
                #     'size': row.xpath('td[2]//text()').extract_first(),
                #     'shakhe': row.xpath('td[4]//text()').extract_first(),
                #     'weight': row.xpath('td[5]//text()').extract_first(),
                #     'length' : row.xpath('td[5]//text()').extract_first(),
                #     'company' : row.xpath('td[6]//text()').extract_first(),
                #     'location' : row.xpath('td[6]//text()').extract_first(),
                #     'price' : row.xpath('td[8]//text()').extract_first()
                # })
            break

    def milgerd_parse(self, response):
 
        for res in response.css('table.tablepress'):

            for row in res.xpath('tbody//tr'):
                
                if row.xpath('td[1]//text()').extract_first() == None:
                    continue
                
                if self.milgerd_type == 'ajdar':


                    for count, obj in enumerate(row.xpath('td//text()'), 1):
                        data = obj.get()
          

                        if "متری" in data:
                            lenght = row.xpath(f'td[{count}]//text()').extract_first()
                           
                        elif re.match("^A",data):
                            
                            {'name': 'میلگرد 12 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '193000'}
                            {'name': 'میلگرد 14 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}
                            {'name': 'میلگرد 16 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}
                            {'name': 'میلگرد 18 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}
                            {'name': 'میلگرد 20 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}
                            {'name': 'میلگرد 22 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}
                            {'name': 'میلگرد 25 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}
                            {'name': 'میلگرد 28 قائم', 'analyse': 'کارخانه', 'lenght': 'A3', 'price': '191000'}

                            if "ظفر بناب" in row.xpath('td[1]//text()').extract_first():
                                count -=1

                            elif "آناهیتا" in row.xpath('td[1]//text()').extract_first():
                                count -= 1

                            elif "قائم" in row.xpath('td[1]//text()').extract_first():
                                if "10" in row.xpath('td[1]//text()').extract_first():
                                    count +=1
                                count -= 1

                            elif "شاهرود" in row.xpath('td[1]//text()').extract_first():
                                if "8" in row.xpath('td[1]//text()').extract_first():
                                    count +=1
                                count -=1

                            elif "سیرجان حدید" in row.xpath('td[1]//text()').extract_first():
                                count -=1

                            elif "سپهر" in row.xpath('td[1]//text()').extract_first():
                                if "12" in row.xpath('td[1]//text()').extract_first():
                                    count +=1
                                count -=1

                           
                           

                            analyse = row.xpath(f'td[{count}]//text()').extract_first()
                            

                        elif "00" in data or "تماس بگیرید" in data :
                            
                            if "ذوب آهن" not in row.xpath('td[1]//text()').extract_first():
                                if "شاهین" in row.xpath('td[1]//text()').extract_first()\
                                    or "سرمد" in row.xpath('td[1]//text()').extract_first() \
                                        or "صبا" in row.xpath('td[1]//text()').extract_first() \
                                            or "میلگرد 8 شاهرود" == row.xpath('td[1]//text()').extract_first() \
                                                or "میلگرد 12 سپهر ایرانیان A3" == row.xpath('td[1]//text()').extract_first() \
                                                    or "کویر" in row.xpath('td[1]//text()').extract_first() \
                                                        or "سیادن" in row.xpath('td[1]//text()').extract_first() \
                                                            or "روهین" in row.xpath('td[1]//text()').extract_first() \
                                                                or "نورد گرم" in row.xpath('td[1]//text()').extract_first() \
                                                                    or "میانه" in row.xpath('td[1]//text()').extract_first() \
                                                                        or "کیان" in row.xpath('td[1]//text()').extract_first() \
                                                                            or "فایکو" in row.xpath('td[1]//text()').extract_first() \
                                                                                or "جهان" in row.xpath('td[1]//text()').extract_first() \
                                                                                    or "ارگ" in row.xpath('td[1]//text()').extract_first() \
                                                                                        or "بردسیر" in row.xpath('td[1]//text()').extract_first() \
                                                                                            or "احرامیان" in row.xpath('td[1]//text()').extract_first() \
                                                                                                or "بردسیر" in row.xpath('td[1]//text()').extract_first() \
                                                                                                    or "درپاد" in row.xpath('td[1]//text()').extract_first() \
                                                                                                        or "هیربد" in row.xpath('td[1]//text()').extract_first() \
                                                                                                            or "فولاد" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                or "یزد" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                    or "جهان" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                        or "خرمدشت" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                            or "هشترود" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                or "احرامیان" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                    or "تیکمه" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                        or "نیک صدرا" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                            or "نیک صدرا" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                or "نیک صدرا" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                    or "کیان فولاد" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                        or "قزوین" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                            or "فولاد صائب" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                or "آریا ذوب" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                    or "فولاد معراج" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                        or "آریا ذوب" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                            or "گلستان" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                                or "کوثر اهواز" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                                    or "گلستان" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                                        or "خلیج فارس" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                                            or "نورد نوین" in row.xpath('td[1]//text()').extract_first() \
                                                                                                                                                                                                or "پارس آرمان" in row.xpath('td[1]//text()').extract_first() :

                                    pass
                                else:
                                    count -=1
                            
                            


                            price = row.xpath(f'td[{count}]//text()').extract_first()
                          
                    
                    #time.sleep(1)
                       
                    print({
                        'name' : row.xpath('td[1]//text()').extract_first(),
                        'analyse': analyse,
                        'lenght': row.xpath('td[2]//text()').extract_first(),
                        'price' : price
                        
                    })
                

                elif self.milgerd_type == 'ipe':
                   pass
                  