import scrapy
import json
import requests
import re
from xiecheng.items import HotelInfoItem,CommentItem
import xiecheng.myutils as mu
import time
import xiecheng.settings

class HotelSpider(scrapy.Spider):
    name = 'hotel'
    allowed_domains = ['ctrip.com']
    start_urls = ['http://m.ctrip.com/restapi/soa2/21881/json/HotelSearch?testab=']
    hotel_detail_url='https://hotels.ctrip.com/hotels/detail/?hotelId='
    hotel_price_url='https://m.ctrip.com/restapi/soa2/21881/json/rateplan?testab='
    download_delay = 0.2

    def read_cfg(self):
        with open('cfg.json', 'r') as f:
            cfg = json.load(f)
        return cfg
    
    def save_cfg(self, cfg):
        with open('cfg.json', 'w') as f:
            json.dump(cfg, f)

    def set_value(self,json_obj,key,value):
        json_obj.get(key)
        json_obj[key]=value

    def __init__(self):
        progress = self.read_cfg()['progress']
        self.page_no=int(progress['currentPage'])
        self.option_id=int(progress['currentOpt'])
        super().__init__()


    def start_requests(self):
        
        while self.option_id<100:
            while self.page_no<100:
                start_time = time.time()
        # if True:
                print('option_id:',self.option_id,'page_no:',self.page_no)
                testab = mu.get_testab()
                hotelUuidKey = mu.get_hotelUuidKey()
                payload = json.dumps({
                "searchCondition": {
                    "sortType": "1",
                    "adult": 1,
                    "child": 0,
                    "age": "",
                    "pageNo": self.page_no,
                    "optionType": "City",
                    "optionId": '{}'.format(self.option_id),
                    "lat": 0,
                    "destination": "",
                    "keyword": "",
                    "cityName": "上海",
                    "lng": 0,
                    "cityId": 2,
                    "checkIn": "2024-11-17",
                    "checkOut": "2024-11-18",
                    "timeOffset": 28800
                },
                "head": {
                    "HotelExtension": {
                        "hotelUuidKey": hotelUuidKey
                }}
                })
                yield scrapy.Request(url=self.start_urls[0]+testab, method='POST', body=payload, headers={'Content-Type': 'application/json'},callback=self.parse_hotel_ids )
                end_time = time.time()
                print('request hotels cost time:', end_time - start_time)
                self.page_no+=1
                cfg = self.read_cfg()
                self.set_value(cfg['progress'],'currentPage',self.page_no)
                self.set_value(cfg['progress'],'currentOpt',self.option_id)
                self.set_value(cfg['progress'],str(self.option_id),str(self.page_no))
                self.save_cfg(cfg)
                
            self.option_id+=1
            self.page_no=1


    def request_hotel_rateplan(self, hotel_id):
        start_time = time.time()
        testab = mu.get_testab()
        hotelUuidKey=mu.get_hotelUuidKey()
        payload = json.dumps({
        "checkIn": "2024-11-18",
        "checkOut": "2024-11-19",
        "priceType": "",
        "adult": 1,
        "popularFacilityType": "",
        "mpRoom": "",
        "fgt": "",
        "hotelUniqueKey": "",
        "child": 0,
        "roomNum": 1,
        "masterHotelId": hotel_id,
        "age": "",
        "cityId": "2",
        "roomkey": "",
        "minCurr": "",
        "minPrice": "",
        "hotel": "72789489",
        "filterData": [],
        "guestCountFilterType": 1,
        "genk": True,
        "genKeyParam": {
            "a": hotel_id,
            "b": "2024-11-18",
            "c": "2024-11-19",
            "d": "zh-cn",
            "e": 2
        },
        "head": {
            "Locale": "zh-CN",
            "Currency": "CNY",
            "Device": "PC",
            "Group": "ctrip",
            "ReferenceID": "",
            "UserRegion": "CN",
            "AID": None,
            "SID": None,
            "Ticket": "",
            "UID": "",
            "IsQuickBooking": "",
            "ClientID": "",
            "OUID": None,
            "TimeZone": "8",
            "Version": "",
            "HotelExtension": {
                "WebpSupport": True,
                "group": "CTRIP",
                "Qid": None,
                "hasAidInUrl": False,
                "hotelUuidKey": hotelUuidKey 
                },
            "Frontend": {
                "sessionID": "13",
                "pvid": "3"
            },
        }
        })    
        headers ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        
        
        
        response = requests.request("POST", self.hotel_price_url+testab, headers=headers, data=payload)
        # print(response.text)
        res_data = json.loads(response.text)
        end_time = time.time()
        print('request_hotel_rateplan cost time:', end_time-start_time)
        return res_data

    def parse_hotel_ids(self, response):
        # print(response.text)
        start_time = time.time()
        print(response.text)
        try:
            hotel_list = json.loads(response.text)['Response']['hotelList']['list']
        except KeyError as e:
            self.option_id+=1
            self.page_no=1
            return
        hotel_ids = []
        for hotel in hotel_list:
            hotel_ids.append(hotel['base']['hotelId'])
        # print(hotel_ids)
        for hotel_id in hotel_ids:
            yield scrapy.Request(url=self.hotel_detail_url+str(hotel_id), callback=self.parse_hotel_details )
        # yield scrapy.Request(url=self.hotel_detail_url+str(hotel_ids[0]), callback=self.parse_hotel_details)
        end_time = time.time()
        print('parse_hotel_ids cost time:', end_time-start_time)

    def parse_hotel_details(self, response):
        start_time = time.time()
        script_text = response.xpath('//script[@type="text/javascript"]/text()').extract()[2]
        # print(script_text)
        hotel_data=json.loads('{'+re.findall(r'window.IBU_HOTEL={(.*?)};', script_text)[0]+'}')['initData']
        hotel_info_item = HotelInfoItem()
        base_data = hotel_data['base']
        position_data = hotel_data['position']
        comment_data = hotel_data['comment']
        initial_review_data = hotel_data['initialReview']
        try:
            facility_data = hotel_data['hotFacility']['list']
        except Exception as e:
            pass
        initial_review_data = hotel_data['initialReview']
        hotel_info_item['id'] = base_data['masterHotelId']
        # print(hotel_info_item['id'])
        hotel_info_item['name'] = base_data['hotelName']
        hotel_info_item['comment_num'] = initial_review_data['ReviewBaseInfo']['totalReviews']
        # calculate the lowest price
        rooms_info = self.request_hotel_rateplan(base_data['masterHotelId'])['Response']['baseRooms']
        # self.request_hotel_rateplan(base_data['masterHotelId'])
        sale_rooms = []
        
        for room in rooms_info:
            sale_rooms += room['saleRoom']
        start_price = int(sale_rooms[0]['base']['availParam']['comparingAmount'])
        for room in sale_rooms:
            cur_price = int(room['base']['availParam']['comparingAmount'])
            if cur_price >0 and cur_price < start_price:
                start_price = cur_price
        hotel_info_item['price'] = start_price
        hotel_info_item['city']=base_data['cityName']
        hotel_info_item['area']=position_data['poi']
        hotel_info_item['address']=position_data['address']
        hotel_info_item['lat']=position_data['lat']
        hotel_info_item['lng']=position_data['lng']
        hotel_info_item['rating']=comment_data['score']
        hotel_info_item['environmental_rating']=comment_data['categoryScore'][0]['itemScore']
        hotel_info_item['health_rating']=comment_data['categoryScore'][1]['itemScore']
        hotel_info_item['service_rating']=comment_data['categoryScore'][2]['itemScore']
        hotel_info_item['facility_rating']=comment_data['categoryScore'][3]['itemScore']
        hotel_info_item['tag']=' '.join([i['facilityName'] for i in facility_data])
        end_time = time.time()
        print('parse_hotel_details cost time:', end_time-start_time)
        yield hotel_info_item
        reviews = initial_review_data['ReviewList']
        for review in reviews:
            comment_item = CommentItem()
            comment_item['id'] = review['reviewId']
            comment_item['comment_text']=review['reviewDetails']['reviewContent']
            comment_item['location']=review['ipLocation'].replace('发布于','')
            yield comment_item
