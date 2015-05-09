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

# find_all方法签名：
# def find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs):
# name 表示标签的名称
# attrs 表示标签的属性名
# recursive 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
# 如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
# text 表示标签中的内容，text 参数可以搜文档中的字符串内容. 与name参数的可选值一样,
#      text 参数接受字符串,正则表达式,列表,方法和True
# limit 表示限制返回的结果数量

# name 分别接受 字符串,正则表达式,列表, 方法和True
print "##############name接受字符串类型参数:"
for item in soup.find_all("title"):
    print item

print "##############name接受正则表达式类型参数:"
for item in soup.find_all(name=re.compile("le")):
    print item

print "##############name接受列表类型参数:"
for item in soup.find_all(["title", "span"]):
    print item

print "##############name接受方法类型:"


def has_5_chars(name):
    """
    :param name: 遍历的标签
    :return: 标签名长度为5的标签
    """
    return name is not None and type(name) == bs4.element.Tag and len(name.name) == 1

for item in soup.find_all(name=has_5_chars):
    print item.name, item.attrs

print "##############name接受True类型参数:"
for item in soup.body.p.find_all(name=True):
    print item

print "##############attrs的值字典类型:"
for child in soup.find_all("a", attrs={"id": "link3", "class": "sister"}):
    print child.string

print '##############限制结果的返回数'
for child in soup.find_all("a", "sister", limit=3):
    print child.string

print '##############find_all(["a", "p"]'
# 定位标签名为a或者p的标签
for child in soup.find_all(["a", "p"]):
    print child.name, child.attrs

print '##############find_all(re.compile("t")'
# 定位标签名包含t的标签
for tag in soup.find_all(re.compile("t")):
    print(tag.name)

print '##############find_all("a",text=)'
# 定位标签名为a且标签内容含有Lacie的标签
for tag in soup.find_all("a", text=re.compile("Lacie")):
    print tag.name, tag.string

print '##############find_all("a", "sister")'
# 定位标签名为a且属性名为sister的标签
for tag in soup.find_all("a", "sister"):
    print tag.name, tag.string

print '##############根据属性名查找（1）:'
# 定位属性名为sister的标签（注意：由于class是python的关键词，所以需要写成class_='*'）
# 但是通过 class_ 参数搜索有指定CSS类名的tag 是从Beautiful Soup的4.1.1版本才开始；
for tag in soup.find_all(class_="sister"):
    print tag.name, tag.string

print '##############根据属性名查找（2）:'
for tag in soup.find_all(id=re.compile("link"), limit=3):
    print tag.name, tag.string

# find_all() 几乎是Beautiful Soup中最常用的搜索方法, 所以我们定义了它的简写方法.
# BeautifulSoup对象 和 tag对象可以被当作一个方法来使用
# find_all的简写方法
print '##############简写find_all:'
for tag in soup(class_="sister", limit=1):
    print tag.name, tag.string

# 当设置limit=1，等价于使用find()方法
# 区别：
# 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表（能够 for in 遍历）,而find()方法直接返回结果.
# find_all() 方法没有找到目标是返回空列表, find()方法找不到目标时,返回 None .
print '##############find:'
item_tag = soup.find(class_="sister")
print item_tag, item_tag.string

print "body中id='link2'的标签：", soup.body.find_all(id="link2")
# 简写：
print "body中id='link2'的标签：", soup.body(id="link2")