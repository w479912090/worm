import urllib.request
import urllib.parse

# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.read().decode('utf-8'))

# data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding = 'utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data = data)
# print(response.read())

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# username = 'username'
# password = 'password'
# url = 'http://localhost/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

from urllib.request import ProxyHandler

# proxy_handler = ProxyHandler({
#     'http': 'http://10.42.3.57',
#     'https': 'http://10.42.3.57'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

import http.cookiejar

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name,'=', item.value)

#以文本形式保存cookies
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
#LWPCookieJar同样可以读取和保存Cookies
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

#99乘法表
# print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))