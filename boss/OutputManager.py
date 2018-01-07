#!/usr/bin/env python3
from elasticsearch import Elasticsearch

class OutputManager(object):
    def __init__(self):
        self._es= Elasticsearch([{'host':'203.76.214.3','port':9000}])
    #添加数据到ES
    def _add_data_to_es(self,data):
        try:
            if data is None:
                return
                # 如果索引不存在，则创建索引
            if self._es.indices.exists(index='recruit') is not True:
                self._es.indices.create(index='recruit')
                # self._es.indices.create(index="douban")
            # 将refresh设为true，使得添加的文档可以立即搜索到；
            self._es.index(index="recruit",doc_type="boss",body={"url":data["url"],"title":data["title"],"wages":data["wages"], "place":data["place"],"experience":data["experience"],"education":data["education"],"tags":data["tags"],"content":data["content"],"company_name":data["company_name"],"company_tag":data["company_tag"],"company_url":data["company_url"],"img":data["img"],"location":data["location"]})
            # res = self._es.get(index="douban", doc_type="boss", id=01)
            # 根据url查询
            res = self._es.search(index="recruit",doc_type="boss",body={"query": {"match": {'url':data["url"]}}})
            print(res)
        except Exception as e:
            print("error:" + str(e))
    #根据url删除数据
    def _del_data_by_url(self,url):
        self._es.delete_by_query(index="recruit",body={"query": {"match": {'url':url}}})
        res = self._es.search(index="recruit", doc_type="boss", body={"query": {"match": {'url': url}}})
        print(res)
    #删除所有数据
    def _del_data_by_all(self):
        res=self._es.delete_by_query(index="recruit",doc_type="boss",body={"query": {"match_all": {}}})
        return res

    #根据URL查询
    def _query_data_by_url(self,url):
        res = self._es.search(index="recruit", doc_type="boss", body={"query": {"match": {'url': url}}})
        print(res)
        return res
    #查询所有文档
    def _query_data_by_all(self):
        res=self._es.search(index="recruit", doc_type="boss", body={"query": {"match_all": {}}})
        return res
if __name__ == '__main__':
    out=OutputManager()
    res=out._del_data_by_all()
    print(res)
