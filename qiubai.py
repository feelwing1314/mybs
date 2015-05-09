# -*- coding:UTF-8 -*-
########################
#
# Created on 2015-05-01
# @author: zhenfei.wang

# 重要知识点：
# pattern = re.compile('<h1.*?class="core_title_txt.*?".*?>(.*?)</h1>', re.S)
# items = re.findall(pattern, content)
#    for item in items:
#       print item[0], item[1]
########################

import urllib2
from bs4 import BeautifulSoup
import re

page = 1
url = "http://www.qiushibaike.com/hot/page/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    # 如果request中没有带header，那么会报错
    req = urllib2.Request("{0}{1}".format(url, str(page)), headers=headers)
    resp = urllib2.urlopen(req)
    # 将页面转化为UTF-8编码
    content = resp.read().decode('utf-8')
    soup = BeautifulSoup(content)
    # print soup.prettify()

    # 现在我们想获取发布人，发布日期，段子内容，以及点赞的个数。

    state = """
    正则表达式说明：

    1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，
        也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。

    2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就
    代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

    3）re.S 标志代表在匹配时为点任意匹配模式，点.也可以代表换行符。

    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?</div>.*?' +
                         '<div.*?class="content".*?>(.*?)</div>.*?' +
                         '<div.*?class="thumb".*?>.*?<a.*?>.*?<img.*?src="(.*?)".*?alt="(.*?)".*?>.*?</a>.*?</div>.*?' +
                         '<div.*?class="stats.*?>.*?<i.*?class="number">(.*?)</i>.*?</div>.*?', re.S)

    #图片不一定有，所以不能写成第三行那样'<div.*?class="thumb".*?>***,否则运行有问题

    """

    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?</div>.*?'
                         '<div.*?class="content".*?>(.*?)</div>'
                         '(.*?)'
                         '<div.*?class="stats.*?>.*?<i.*?class="number">(.*?)</i>.*?</div>.*?', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print "author: ", item[0]
        print "糗事:   ", item[1]
        # TODO 无法取得图片内容
        print "图片detail:   ", item[2]
        # 是否含有图片
        have_img = re.search("img", item[2])
        # 如果不含有图片，把它加入list中
        if have_img:
            print "图片URL:   ", BeautifulSoup(item[2]).img['src']

        print "点赞:   ", item[3]


        print "#################################"

except urllib2.URLError, e:
    print e.code
    print e.reason
