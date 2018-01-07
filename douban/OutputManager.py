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
            if self._es.indices.exists(index='douban') is not True:
                self._es.indices.create(index='douban')
                # self._es.indices.create(index="douban")
            # 将refresh设为true，使得添加的文档可以立即搜索到；
            self._es.index(index="douban",doc_type="tushu",body={"url":data["url"],"title":data["title"],"content":data["content"]})
            # res = self._es.get(index="douban", doc_type="tushu", id=01)
            # 根据url查询
            res = self._es.search(index="douban",doc_type="tushu",body={"query": {"match": {'url':data["url"]}}})
            print(res)
        except Exception as e:
            print("error:" + str(e))
    #根据url删除数据
    def _del_data_by_url(self,url):
        self._es.delete_by_query(index="douban",body={"query": {"match": {'url':url}}})
        res = self._es.search(index="douban", doc_type="tushu", body={"query": {"match": {'url': url}}})
        print(res)
    #删除所有数据
    def _del_data_by_all(self):
        res=self._es.delete_by_query(index="douban",doc_type="tushu",body={"query": {"match_all": {}}})
        return res

    #根据URL查询
    def _query_data_by_url(self,url):
        res = self._es.search(index="douban", doc_type="tushu", body={"query": {"match": {'url': url}}})
        print(res)
        return res
    #查询所有文档
    def _query_data_by_all(self):
        res=self._es.search(index="douban", doc_type="tushu", body={"query": {"match_all": {}}})
        return res
if __name__ == '__main__':
    out=OutputManager()
    res=out._del_data_by_all()
    print(res)
    # out._del_data_by_url("www.baidu.com")
    # out._add_data_to_es(data={"url":"www.baidu.com","title":"放风筝的人","content":"555555555555555555555555"})
    # print(out._query_data_by_all())
