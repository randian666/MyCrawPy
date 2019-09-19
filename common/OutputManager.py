#!/usr/bin/env python3
from elasticsearch import Elasticsearch
from elasticsearch import helpers

class OutputManager(object):
    def __init__(self,index,type):
        self.index=index
        self.type=type
        self._es = Elasticsearch(['39.97.240.232'], http_auth=('elastic', 'wuyuexpack'), timeout=9200)
    #添加数据到ES
    def _add_data_to_es(self,data):
        try:
            if data is None:
                return
                # 如果索引不存在，则创建索引
            if self._es.indices.exists(index=self.index) is not True:
                self._es.indices.create(index=self.index)
                # self._es.indices.create(index="douban")
            # 将refresh设为true，使得添加的文档可以立即搜索到；
            for m in data:
                self._es.index(index=self.index,doc_type=self.type,id=m['url'],body=m)
        except Exception as e:
            print("error:" + str(e))
    #根据url删除数据
    def _del_data_by_url(self,url):
        self._es.delete_by_query(index=self.index,body={"query": {"match": {'url':url}}})
        res = self._es.search(index=self.index, doc_type=self.type, body={"query": {"match": {'url': url}}})
        print(res)
    #删除所有数据
    def _del_data_by_all(self):
        res=self._es.delete_by_query(index=self.index,doc_type=self.type,body={"query": {"match_all": {}}})
        return res

    #根据URL查询
    def _query_data_by_url(self,url):
        res = self._es.search(index=self.index, doc_type=self.type, body={"query": {"match": {'url': url}}})
        print(res)
        return res
    #查询所有文档
    def _query_data_by_all(self):
        res=self._es.search(index=self.index, doc_type=self.type, body={"query": {"match_all": {}}})
        return res
if __name__ == '__main__':
    out=OutputManager('datum_index','datum')
    # out._add_listdata_to_es()
    res=out._del_data_by_all()
    print(res)
