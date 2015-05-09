# -*- coding:UTF-8 -*-
# 必须申明编码为UTF-8，否则注释内容不能有中文
__author__ = 'afei'

from bs4 import BeautifulSoup
import bs4
import re

# 这段文档来自bs的官方文档http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
# 得到BeautifulSoup对象, 首先,文档会被转换成Unicode,并且HTML的实例都被转换成Unicode编码，
# 如果通过from_encoding指定了编码，那么转换成指定编码
soup = BeautifulSoup(open('test_forFind.html'), from_encoding='UTF-8')

# CSS选择器：
# CSS选择器非常方便，而且功能强大，如果你仅仅需要CSS选择器的功能,那么直接使用 lxml 也可以,
# 而且速度更快,支持更多的CSS选择器语法,但Beautiful Soup整合了CSS选择器的语法和自身方便使用的API.

print "##############通过标签逐层查找:"
for item in soup.select("html head title"):
    print item

print "##############通过标签逐层(层级关系可以跳跃)查找:"
for item in soup.select("html title"):
    print item

print "##############通过标签查找(指定直接子标签):"
for item in soup.select("html > head > title"):
    print item

print "##############通过标签查找(指定直接子标签的序号，序号从1开始):"
for item in soup.select("body > p:nth-of-type(3)"):
    print item

print "##############找到兄弟节点(这种写法不会把空格包含在内，比next_siblings更实用)"
for item in soup.select("#link1 ~ .sister"):
    print item
print "##############找到第一个兄弟节点"
for item in soup.select("#link1 + .sister"):
    print item

print "##############通过id查找"
print soup.select("#link1")

print "##############通过class查找"
print soup.select(".title")

print "##############通过标签名和标签的id查找"
print soup.select("a#link1")

print "##############通过标签名和标签的class查找"
print soup.select("p.title")

print "##############通过标签名以及属性名查找："
print soup.select("span[style]")

print "##############通过标签名以及属性的值查找："
print "----------属性值精确匹配(1)"
print soup.select('a[href="http://example.com/elsie"]')

print "----------属性值以什么开头(2)"
print soup.select('a[href^="http://example.com/"]')

print "----------属性值以什么结尾(3)"
print soup.select('a[href$="tillie"]')

print "----------属性值包含什么(4)"
print soup.select('a[href*=".com/el"]')
