from datetime import datetime

import requests
from fake_useragent import UserAgent
import uuid
import hmac
import hashlib


headers = {
    "UserAgent": UserAgent().random,
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    'Connection': 'close',  # make sure requests closes the sockets instead of keep-alive!
    'Accept': '*/*',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie2': '$Version=1',
    'Accept-Language': 'en-US',
}

base_url = "https://www.instagram.com/accounts/login/"
url = "https://www.instagram.com/accounts/login/ajax/"

class InstagramLogin:
    
    username = "yogeshwaran01"
    password = "Yogesh2001*"
    
    def __init__(self):
        with requests.session() as self.session:
            res = self.session.get(base_url)
            print(res.cookies)
            self.token = res.cookies['csrftoken']
        
        self.payload = {
            'username': self.username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{self.password}',
            'queryParms': {},
            'optInotOneTap': 'false'
            
        }
        
        headers["x-csrftoken"] = self.token
        
        l_res = self.session.post(url, data=self.payload, headers=headers)
        print(headers)
        
        print(l_res.json())
        