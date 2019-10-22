#!/usr/bin/env python3
from elasticsearch import Elasticsearch

class OutputManager(object):
    def __init__(self):
        self._es = Elasticsearch(['39.97.240.232'], http_auth=('elastic', 'wuyuexpack'), timeout=9200)
    #添加数据到ES
    def _add_data_to_es(self,jsonData):
        try:
            if jsonData is None:
                return
                # 如果索引不存在，则创建索引
            if self._es.indices.exists(index='dujiaoshou') is not True:
                self._es.indices.create(index='dujiaoshou')
            # 将refresh设为true，使得添加的文档可以立即搜索到；
            self._es.index(index="dujiaoshou",doc_type="content",body=jsonData)
        except Exception as e:
            print("error:data is{},error is {}".format(jsonData,str(e)))
    #根据url删除数据
    def _del_data_by_url(self,url):
        self._es.delete_by_query(index="dujiaoshou",body={"query": {"match": {'url':url}}})
        res = self._es.search(index="dujiaoshou", doc_type="content", body={"query": {"match": {'url': url}}})
        print(res)
    #删除所有数据
    def _del_data_by_all(self):
        res=self._es.delete_by_query(index="dujiaoshou",body={"query": {"match_all": {}}})
        return res

    #根据URL查询
    def _query_data_by_url(self,url):
        res = self._es.search(index="dujiaoshou", doc_type="content", body={"query": {"match": {'url': url}}})
        print(res)
        return res
    #查询所有文档
    def _query_data_by_all(self):
        res=self._es.search(index="dujiaoshou", doc_type="content", body={"query": {"match_all": {}}})
        return res
if __name__ == '__main__':
    out=OutputManager()
    res=out._del_data_by_all()
    # print(res)

