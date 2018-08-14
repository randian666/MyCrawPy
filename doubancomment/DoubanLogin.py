
import requests
# import html5lib
import re
from bs4 import BeautifulSoup

class DoubanLogin(object):
    def login(self):
        s = requests.Session()
        url_login = 'https://accounts.douban.com/login'

        formdata = {
            'redir': 'https://www.douban.com',
            'form_email': "*",
            'form_password': "*",
            'login': u'登陆'
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

        r = s.post(url_login, data = formdata, headers = headers)
        content = r.text
        soup = BeautifulSoup(content, 'html.parser')
        captcha = soup.find('img', id = 'captcha_image')#当登陆需要验证码的时候
        if captcha:
            captcha_url = captcha['src']
            re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
            captcha_id = re.findall(re_captcha_id, content)
            print(captcha_id)
            print(captcha_url)
            captcha_text = input('Please input the captcha:')
            formdata['captcha-solution'] = captcha_text
            formdata['captcha-id'] = captcha_id
            r = s.post(url_login, data = formdata, headers = headers)
        with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
            f.write(r.text)
        return s