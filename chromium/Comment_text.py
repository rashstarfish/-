# -*- coding: utf-8 -*-

import phoenixdb
from DrissionPage import Chromium
import csv
import time
import phoenixdb.cursor

database_url = "http://10.21.62.10:2000/"
conn = phoenixdb.connect(database_url, autocommit=True)
cursor = conn.cursor()
# cursor.execute("CREATE TABLE comment_text(id INTEGER PRIMARY KEY,comment_text VARCHAR)")
# print(cursor.fetchall())

cursor.execute("SELECT MAX(id) FROM comment_text")
max_id = cursor.fetchone()[0]
if max_id is None:
    id_counter = 1
else:
    id_counter = max_id + 1

dp = Chromium().latest_tab
# dp.listen.start('json/GetReviewList')
# dp.get('https://hotels.ctrip.com/hotels/detail/?hotelId=369745')
# resp = dp.listen.wait()

# json_data = resp.response.body
# commentList = json_data['Response']['ReviewList']


dp.listen.start('json/GetReviewList')
dp.get('https://hotels.ctrip.com/hotels/detail/?hotelId=369745')
for page in range(1,300):

    print(f'正在采集第{page}页的数据内容')
    resp = dp.listen.wait()

    json_data = resp.response.body

    commentList = json_data['Response']['ReviewList']

    for index in commentList:
        dit ={
            'id':id_counter,
            'comment_text':index['reviewDetails']['reviewContent']
        }
        id_counter +=1
        print(dit)
        time.sleep(2)
        upsert_sql = """
            UPSERT INTO comment_text (id,comment_text)
            VALUES (?, ?)
            """
        cursor.execute(upsert_sql, tuple(dit.values()))
    next_page_button = dp.ele('@class=forward active', timeout=10)
    next_page_button.click()


cursor.close()
conn.close()
