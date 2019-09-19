#!/usr/bin/env python3
from bs4 import BeautifulSoup


#获取指定页面的链接和内容
def _parse_jobdetail(html_content,html_encode="utf-8"):
    soup = BeautifulSoup(html_content, "html.parser", from_encoding=html_encode)
    job_detail = soup.select_one(".job_detail>.job_bt")
    content=""
    content_html=""
    if job_detail is not None:
        content=job_detail.get_text()
        content_html=job_detail.prettify()
    return content,content_html