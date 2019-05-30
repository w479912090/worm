from urllib.parse import urlparse

#urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
'''
返回结果是一个ParseResult类型的对象，它包含6部分，分别是scheme、netloc、path、params、query和fragment
urlparse()方法将其拆分成了6部分。大体观察可以发现，解析时有特定的分隔符。比如，://前面的就是scheme，代表协议；第一个/前面便是netloc，即域名；问号?前面是params，代表参数
'''

#urlunparse
from urllib.parse import urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=5', 'comment']
print(urlunparse(data))
'''
有了urlparse()，相应地就有了它的对立方法urlunparse()。它接受的参数是一个可迭代对象，但是它的长度必须是6，否则会抛出参数数量不足或者过多的问题
'''

#urlsplit
from urllib.parse import urlsplit
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
'''
这个方法和urlparse()方法非常相似，只不过它不再单独解析params这一部分，只返回5个结果。上面例子中的params会合并到path中
'''

#urlunsplit
from urllib.parse import urlunsplit
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
'''
与urlunparse()类似，它也是将链接各个部分组合成完整链接的方法，传入的参数也是一个可迭代对象，例如列表、元组等，唯一的区别是长度必须为5
'''

#urljoin
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
'''
生成链接还有另一个方法，那就是urljoin()方法。我们可以提供一个base_url（基础链接）作为第一个参数，将新的链接作为第二个参数，
该方法会分析base_url的scheme、netloc和path这3个内容并对新链接缺失的部分进行补充
base_url提供了三项内容scheme、netloc和path。如果这3项在新的链接里不存在，就予以补充；如果新的链接存在，就使用新的链接的部分。
而base_url中的params、query和fragment是不起作用的
'''

#urlencode序列化
from urllib.parse import urlencode
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
'''
先声明了一个字典来将参数表示出来，然后调用urlencode()方法将其序列化为GET请求参数
'''

#parse_qs反序列化
from urllib.parse import parse_qs
query = 'name=germy&age=22'
print(parse_qs(query))
'''
如果我们有一串GET请求参数，利用parse_qs()方法，就可以将它转回字典
'''

#parse_qsl
from urllib.parse import parse_qsl
query = 'name=germy&age=22'
print(parse_qsl(query))
'''
用于将参数转化为元组组成的列表
'''

#quote
from urllib.parse import quote
keyword = '壁纸'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(keyword)
'''
该方法可以将内容转化为URL编码的格式
'''

#unquote
from urllib.parse import unquote
url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
'''
可以进行URL解码
'''