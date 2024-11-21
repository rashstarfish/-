# -*- coding: utf-8 -*-

import phoenixdb
from DrissionPage import Chromium
import csv
import time
import phoenixdb.cursor

database_url = "http://10.21.62.10:2000/"
conn = phoenixdb.connect(database_url, autocommit=True)
cursor = conn.cursor()
# print(cursor.fetchall())

city_ids = [25]
cursor.execute("SELECT MAX(id) FROM hotels_info")
max_id = cursor.fetchone()[0]
if max_id is None:
    id_counter = 1
else:
    id_counter = max_id + 1

dp = Chromium().latest_tab

dp.listen.start('json/HotelSearch')


for city_id in city_ids:
    url = f'https://hotels.ctrip.com/hotels/listPage?city={city_id}'
    dp.get(url)

    for page in range(1,30):
        print(f'正在采集第{page}页的数据内容')
        if page>4:
            next_page = dp.ele('css:.btn-box span')
            if next_page.text == '搜索更多酒店':
                next_page.click()


        resp = dp.listen.wait()

        json_data = resp.response.body

        hotelList = json_data['Response']['hotelList']['list']

        for index in hotelList:
            comment_num = index['comment'].get('content','暂无评分') if 'comment' in index else '暂无评分'
            # rating = index['score'].get('number','暂无评分') if 'score' in index else '暂无评分'
            # environment_rating = index.get('score', {}).get('subScore', [{}])[0].get('number', '暂无评分')
            # health_rating = index.get('score', {}).get('subScore', [{}])[1].get('number', '暂无评分')
            # service_rating = index.get('score', {}).get('subScore', [{}])[2].get('number', '暂无评分')
            # facility_rating =  index.get('score', {}).get('subScore', [{}])[3].get('number', '暂无评分')

            if 'score' in index:
                rating = index['score'].get('number', '暂无评分')
                sub_score = index['score'].get('subScore', [])
                
                # 安全地访问 'subScore' 列表的元素
                if len(sub_score) > 0:
                    environment_rating = sub_score[0].get('number', '暂无评分')
                if len(sub_score) > 1:
                    health_rating = sub_score[1].get('number', '暂无评分')
                if len(sub_score) > 2:
                    service_rating = sub_score[2].get('number', '暂无评分')
                if len(sub_score) > 3:
                    facility_rating = sub_score[3].get('number', '暂无评分')
            dit ={
                'id':id_counter,
                'name':index['base']['hotelName'],
                'comment_num':comment_num,
                'price':index['money']['price'],
                'city':index['position']['cityName'], 
                'area':index['position']['area'],
                'address':index['position']['address'],
                'lat':index['position']['lat'],
                'log':index['position']['lng'],
                'rating':rating,
                'Environmental_rating':environment_rating,
                'Health_rating':health_rating,
                'service_rating':service_rating,
                'facility_rating':facility_rating,
                'tag':' '.join(index['base']['tags'])
            }   

            id_counter += 1
            print(dit)
            dp.scroll.to_bottom()
            time.sleep(2)
            
            upsert_sql = """
            UPSERT INTO hotels_info (id, name, comment_num, price, city, area, address, lat, log, rating, Environmental_rating, Health_rating, service_rating, facility_rating, tag)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(upsert_sql, tuple(dit.values()))





cursor.close()
conn.close()

