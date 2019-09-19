#!/usr/bin/env python3
from bs4 import BeautifulSoup


#获取指定页面的链接和内容
def _parse_jobdetail(html_content,html_encode="utf-8"):
    soup = BeautifulSoup(html_content, "html.parser", from_encoding=html_encode)
    job_detail = soup.select_one("div.content_l.fl")
    content=""
    if job_detail is not None:
        content=job_detail.get_text()
    return content