#!/usr/bin/env python3
import json

class HtmlParser(object):
    #获取指定页面符合要求的内容 JSON
    def _parse_data(self,content,html_encode="utf-8"):
        if content is None:
            return
        jsonContent = json.loads(content)
        return jsonContent
        # 获取数据
