#!/usr/bin/env python3
from elasticsearch import Elasticsearch

class OutputManager(object):
    def __init__(self):
        self._es= Elasticsearch([{'host':'140.143.240.63','port':9345}])
    #添加数据到ES
    def _add_data_to_es(self,data):
        try:
            if data is None:
                return
                # 如果索引不存在，则创建索引
            if self._es.indices.exists(index='star_index') is not True:
                self._es.indices.create(index='star_index')
                # self._es.indices.create(index="douban")
            # 将refresh设为true，使得添加的文档可以立即搜索到；
            self._es.index(index="star_index",doc_type="star",body={"url":data["url"],"source":data["source"],"created":data["created"], "star_pic":data["star_pic"],"name":data["name"],"wiki_content":data["wiki_content"],"star_info":data["star_info"],"star_image":data["star_image"],"star_related":data["star_related"]})

        except Exception as e:
            print("error:" + str(e))
    #根据url删除数据
    def _del_data_by_url(self,url):
        self._es.delete_by_query(index="star_index",body={"query": {"match": {'url':url}}})
        res = self._es.search(index="star_index", doc_type="star", body={"query": {"match": {'url': url}}})
        print(res)
    #删除所有数据
    def _del_data_by_all(self):
        res=self._es.delete_by_query(index="star_index",doc_type="star",body={"query": {"match_all": {}}})
        return res

    #根据URL查询
    def _query_data_by_url(self,url):
        res = self._es.search(index="star_index", doc_type="star", body={"query": {"match": {'url': url}}})
        print(res)
        return res
    #查询所有文档
    def _query_data_by_all(self):
        res=self._es.search(index="star_index", doc_type="star", body={"query": {"match_all": {}}})
        return res
if __name__ == '__main__':
    out=OutputManager()
    res=out._del_data_by_all()
    print(res)
