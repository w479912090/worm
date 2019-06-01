#coding=utf-8

#文件上传
import requests
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files = files)
# print(r.text)

#Cookies
r = requests.get('http://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key, '=', value)

headers = {
    'Cookie': '_zap=90d583da-1b61-4dcf-9c4f-089c776862be; d_c0="AADptf7_WQ-PTq0w-0XoFqXEFLPDb5NPlBw=|1556517834"; _xsrf=sOvTUJ9xvSEIwe2VEeA6YzTt7FATPctw; q_c1=2aca489ed98a4a76a4d0058d4c435894|1557886184000|1557886184000; l_cap_id="ZGFhZmZkNDcyZjdkNGNkMGE2MThiODA5NTRjZTFhZTg=|1557886239|5c1649cf9d08cb9eca6fbaa29713a9063fa51110"; r_cap_id="NGQ5YTJiZWMyZGUxNDY2YWI2NGY1MWNlNWUzYTA4Yzk=|1557886239|3b5744fd1cd547d3611d6810fb349211f5c01a73"; cap_id="NmE2MTg5Y2Y4YjVlNGE5ODg0NDUwYmVjZGY2YWVkMTk=|1557886239|30fd070ff5fe7c2d1bb18a210572bc0e00b9fe81"; capsion_ticket="2|1:0|10:1558777637|14:capsion_ticket|44:YzFiYjMzZDBkMmM1NDllMGFhMzMwN2RhYTNkNWFhZWI=|6a010dac900ffb3c7036840f7fd34648b77d354910ee221d6fde5b9a7c9b7990"; z_c0="2|1:0|10:1558777657|4:z_c0|92:Mi4xQmRlWERnQUFBQUFBQU9tMV92OVpEeVlBQUFCZ0FsVk5PVjNXWFFEaF9BZUtQdlU4VWtPSDdkWm5Jc3lWeXJrQWNR|9a9077c4671bc7729deb7d075e8c8bee94d2c67e90df22924a6ad2309d7d00da"; tst=r; tgw_l7_route=116a747939468d99065d12a386ab1c5f',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers = headers)
print(r.text)

#会话维持  Session对象
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

#SSL证书验证
#可以使用verify参数控制是否检查此证书。其实如果不加verify参数的话，默认是True，会自动验证
response = requests.get('https://www.12306.cn', verify = False)
print(response.status_code)

from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

import logging
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

#代理设置
# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
# }
# requests.get('https://www.taobao.com', proxies=proxies)
#若代理需要使用HTTP Basic Auth，可以使用类似http://user:password@host:port这样的语法来设置代理
# proxies = {
#     "http": "http://user:password@10.10.1.10:3128/",
# }
# requests.get("https://www.taobao.com", proxies=proxies)

#超时设置
# r = requests.get('https://www.taobao.com', timeout = 1)
# print(r.status_code)
#请求分为两个阶段，即连接（connect）和读取（read）
#如果要分别指定，就可以传入一个元组：
# r = requests.get('https://www.taobao.com', timeout=(5,11, 30))
#如果想永久等待，可以直接将timeout设置为None，或者不设置直接留空，因为默认是None
# r = requests.get('https://www.taobao.com', timeout=None)
# r = requests.get('https://www.taobao.com')

#身份验证
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost', auth = HTTPBasicAuth('username', 'password'))
print(r.status_code)
#可以直接传一个元组，它会默认使用HTTPBasicAuth这个类来认证
r = requests.get('http://localhost', auth=('username', 'password'))
print(r.status_code)

#Prepared_Request
from requests import Request, Session
url = 'http://httpbin.org/post'
data = {
    'name': 'germy'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data = data, headers = headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)