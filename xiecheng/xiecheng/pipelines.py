# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from xiecheng.items import HotelInfoItem,CommentItem
import phoenixdb
import phoenixdb.cursor
from xiecheng.myutils import get_connection

class XiechengPipeline:
    
    def process_item(self, item, spider):
        if isinstance(item, HotelInfoItem):
            # database_url = "http://192.168.230.130:8765/"
            # conn = phoenixdb.connect(database_url, autocommit=True)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("upsert into hotels_info values("+"?,"*14+"?)",tuple([str(item[i]) if i!='id' else item[i] for i in item.keys()]))
            cursor.close()
            print("hotel:{} saved".format(item['id']))
            return item
        if isinstance(item, CommentItem):
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("upsert into comment_text values(?,?,?)",tuple([str(item[i]) if i!='id' else int(item[i]) for i in item.keys()]))
            cursor.close()
            print("comment:{} saved".format(item['id']))
            return item
