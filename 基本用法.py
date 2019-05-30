#coding=utf-8

import requests
r = requests.get('http://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/post')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

r = requests.get('http://httpbin.org/get?name=germy&age=22')
print(r.text)

#用字典存储params
data = {
    'name': 'germy',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)

r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
#调用json()方法，就可以将返回结果是JSON格式的字符串转化为字典
#如果返回结果不是JSON格式，便会出现解析错误，抛出json.decoder.JSONDecodeError异常


#抓取网页
import re
headers = {
    #浏览器标识信息，如果不加这个，知乎会禁止抓取
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('http://www.zhihu.com/explore', headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
print(title)

#抓取二进制数据
# r = requests.get('https://github.com/favicon.ico')
# with open('favion.ico', 'wb') as f:
#     f.write(r.content)

#POST请求
data = {'name': 'germy', 'age': 22}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
#其中form部分就是提交的数据,正确打印说明POST请求成功发送了

#requests还提供了一个内置的状态码查询对象requests.codes
r = requests.get('http://www.jianshu.com', headers = headers)
if not r.status_code == requests.codes.ok:
    print(1)
else:
    print('Request Successfully') 
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')