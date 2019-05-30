'''
Robots协议也称作爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准（Robots Exclusion Protocol），
用来告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取。它通常是一个叫作robots.txt的文本文件，一般放在网站的根目录下
'''

#robots.txt的样例
'''User-agent: *
Disallow: /
Allow: /public/'''
#上面的User-agent描述了搜索爬虫的名称，这里将其设置为*则代表该协议对任何爬取爬虫有效
#Disallow指定了不允许抓取的目录，比如上例子中设置为/则代表不允许抓取所有页面
#Allow一般和Disallow一起使用，一般不会单独使用，用来排除某些限制。现在我们设置为/public/，则表示所有页面不允许抓取，但可以抓取public目录

#禁止爬虫访问任何目录下的代码
'''User-agent: * 
Disallow: /'''

#允许任何爬虫访问任何目录下的代码   直接文件留空也行
'''User-agent: *
Disallow:'''

#禁止所有爬虫访问网站某些目录的代码
'''User-agent: *
Disallow: /private/
Disallow: /tmp/'''

#只允许某一个爬虫访问的代码
'''User-agent: WebCrawler
Disallow:
User-agent: *
Disallow: /'''

#robotparser
#使用robotparser模块来解析robots.txt
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.baidu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'htto://www.baidu.com/search?q=python&page=1&type=collections'))
#利用can_fetch()方法判断了网页是否可以被抓取

#同样可以使用parse()方法执行读取和分析
from urllib.request import urlopen
rp = RobotFileParser()
rp.parse(urlopen('http://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.baidu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'htto://www.baidu.com/search?q=python&page=1&type=collections'))