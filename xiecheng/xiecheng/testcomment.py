import requests
import random
import time
import json
import re


class XieChengRemarkSpider(object):

    def __init__(self, placeid):
        self.placeId = placeid
        # 创建session实例
        self.session = requests.session()
        # 设置请求头
        self.session.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'
        }

    def get_remarks(self, index):
        """
        # https://gs.ctrip.com/html5/you/sight/qingdao5/56337.html
        :param index: 当前爬取页数
        :return: remarks评论响应结果
        """
        # 获取关键参数并且补充请求cookie信息
        self.session.get(f"https://gs.ctrip.com/html5/you/sight/qingdao5/{self.placeId}.html", timeout=10)
        guid = self.session.cookies['GUID']
        # x_traceID = ‘_fxpcqlniredt -’+timestamp + '-' + 随机数
        url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList'
        params={
            '_fxpcqlniredt':guid,
            'x-traceID':f"{guid}-{round(time.time() * 1000)}-{int(1e6 * random.random())}"
        }
        head={
            "auth": "",
            "cid": guid,
            "ctok": "",
            "cver": "1.0",
            "extension": [{'name':"tecode",'value':"h5"}],
            "lang": "01",
            "sid": "8888",
            "syscode": "09",
            "xsid": ""
        }
        post_data = {
            "arg": {
                "channelType": 7,
                "collapseType": 1,
                "commentTagId": 0,
                "pageIndex": index,
                "pageSize": 10,
                "resourceId": self.placeId,
                "resourceType": 11,
                'sourceType':1,
                "sortType": 3,
                "starType": 0,
                'videoImageSize':"700_392"
            },
            "head": head,
            'contentType':'json'
        }
        return self.session.post(url,params=params, data=json.dumps(post_data), timeout=10)

    def parse_remarks(self, xhr):
        # 文本清洗特殊字符的正则表达式
        p = re.compile(r'[^\w，。！？,.、:；℃]')
        result = xhr.json()["result"]['items']
        remarks = [{
            'score': item['score'],
            'content': p.sub('', item['content'].lower()),
            'Locate': item['ipLocatedName'],
            'publishTime': int(item['publishTime'][6:16])
        } for item in result]
        # 注意这时存在某些'content'实际为空值
        return remarks

if __name__ == '__main__':
    xcrs = XieChengRemarkSpider('56337')
    total_count = int(xcrs.get_remarks(1).json()['result']['totalCount'])
    # 总评论页码数除以10如果能够整除就不用加一，如果不能整除，需要取整并且加一
    pages = total_count // 10 if total_count % 10 == 0 else (total_count // 10) + 1
    print(f'合计{total_count}条评论，需要爬取{pages}页。')
    for i in range(1,pages+1):
        time.sleep(random.random()*0.6)
        xhr = xcrs.get_remarks(i)
        try:
            remarks = xcrs.parse_remarks(xhr)
            print(remarks)
        except Exception as e:
            time.sleep(10 + random.random()*5)
            print(e)
            break