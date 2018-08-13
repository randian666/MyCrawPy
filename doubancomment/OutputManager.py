#!/usr/bin/env python3
from elasticsearch import Elasticsearch
import pandas as pd
class OutputManager(object):
    def __init__(self):
        self._es= Elasticsearch([{'host':'203.76.214.3','port':9000}])
    #添加数据到ES
    def _add_data_to_csv(self,data):
        if data is None:
            return
        dfData=pd.DataFrame(data)
        dfData.to_csv("xiebuyazheng.csv", header=False,index=False,mode='a+',encoding='utf_8_sig')
