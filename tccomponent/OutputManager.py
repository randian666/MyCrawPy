#!/usr/bin/env python3
import requests
import json


class OutputManager(object):
    def __init__(self):
        self.blackList=(['TCBase.Data','TCBase.Cache','TCBase.Cache.v2'])
    # 添加数据到config
    def _add_data_to_config(self, jsonData):
        try:
            url = 'http://tccomponent.17usoft.com/configcenterui/modifyData?token=b055363b5fabc6c746db30125c6d8499'
            # 消息头数据
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Content-Length': '214',
                'Content-Type': 'application/json',
                'Cookie': 'UM_distinctid=16a6d357ad3364-0c82210decc2fc-e323069-144000-16a6d357ad46be; _ga=GA1.2.1435867583.1555326491; access_token=507c77ae32d511f42b8984cf6c1bf3a9',
                'Host': 'tccomponent.17usoft.com',
                'Origin': 'http://tccomponent.17usoft.com',
                'Referer': 'http://tccomponent.17usoft.com/configcenterui/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            }
            for conf in jsonData:
                key=conf['key']
                if key in self.blackList:
                    print(key+'在黑名单中不写入该配置')
                    continue
                payload = {'data': {'key': conf['key'],
                                    'group': conf['group'],
                                    'remark': conf['remark'],
                                    'open': 'false',
                                    'parentGroup': '',
                                    'projectName': 'iflight.java.dsf.ipolicytradecore',
                                    'userName': '1201776',
                                    'cacheType': 'add',
                                    'env': 'qa',
                                    'value': conf['value'],
                                    'serverRoom': 'Default'
                                    }}
                print(conf)
                payloadjson=json.dumps(payload)
                print(payloadjson)
                r = requests.post(url, data=payloadjson, headers=headers, verify=False)
                if r.status_code==200:
                    print(key+"，写入成功")
        except Exception as e:
            print("error:data is{},error is {}".format(jsonData, str(e)))


if __name__ == '__main__':
    out = OutputManager()
