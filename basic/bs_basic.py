# -*- coding:UTF-8 -*-
# 必须申明编码为UTF-8，否则注释内容不能有中文
__author__ = 'zhenfei.wang'


from bs4 import BeautifulSoup
import bs4

# 这段文档来自bs的官方文档http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
# 得到BeautifulSoup对象, Beautiful Soup用了 编码自动检测 子库来识别当前文档编码并转换成Unicode编码.
# BeautifulSoup 对象的 .original_encoding 属性记录了自动识别编码的结果(如果通过from_encoding指定了
# 编码，那么就是指定后的编码)
# 对于输出编码，通过Beautiful Soup输出文档时,不管输入文档是什么编码方式,输出编码均为UTF-8编码
soup = BeautifulSoup(open('test.html'), from_encoding='UTF-8')
print soup.original_encoding

# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
# 所有对象可以归纳为4种: Tag(<class 'bs4.element.Tag'>) , NavigableString(<class 'bs4.element.NavigableString'>) ,
# BeautifulSoup(<class 'bs4.BeautifulSoup'>) , Comment(<class 'bs4.element.Comment'>) .
# comment内容与标签之间不能有空格，否则bs认为不是Comment类型
# 获取对象的类型，并判断：
print type(soup.head)
print type(soup.head.title.string)
print type(soup)
print type(soup.body.span.string)

if type(soup.head) == bs4.element.Tag:
    print "head is type of tag."

# 定位标签
print "The tag of head: \n", soup.head

# 获取标签的所有属性/制定属性(注意：html文档没有多值属性，但是xml文档有多值属性，例如<p id="my id"></p>
# 如果在html文档中，那么标签p的属性id的值是my id，而在xml文档中属性id的值是一个属性)
print "The attrs of head: \n", soup.body.attrs
print "The attr id of head: \n", soup.body["id"]

# 获取标签中的内容
# 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点；
# 如果tag只有一个Tag类型子节点,且该Tag类型子节点也只有一个NavigableString类型子节点,那么这个tag也可用.string得到子节点；
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print "The content of head: \n", soup.head.title.string

# 通过点符号取属性的方式只能获得当前名字的第一个tag,例如下面的示例只能获得class=title的p标签，而不能获得class=story的p标签:
print soup.body.p.attrs

print "得到body下面的所有p标签[第1种方法]:"
for item in soup.body.find_all("p"):
    print item.name, item['class']

# .contents 和 .children 属性仅包含tag的直接子节点.
# .contents 和 .children 属性会把空白内容也当做有效的子节点，这点会干扰正常的业务逻辑，需要在编码时注意
# .descendants 属性可以对所有tag的子孙节点进行递归循环

print "得到body下面的所有p标签[第2种方法]:"
index = 1
for child in soup.body.children:
    print "标签编号"+str(index), child
    index += 1

print "##################"

print "得到body下面的所有p标签[第3种方法]:"
index = 1
for child in soup.body.contents:
    print "标签编号"+str(index), child
    index += 1

# .parent得到父节点
# .parents得到所有父节点
print "body的父节点:", soup.body.parent.name

# .next_sibling 和 .previous_sibling 得到兄弟节点（注意：这两个方法会把空节点或者字符串也当做有效的兄弟节点）
print soup.body.p.next_sibling

# .next_siblings 和 .previous_siblings遍历兄弟节点，然后通过type判断类型，从而排除掉兄弟节点中不符合要求的空格和字符串
for item in soup.body.p.next_siblings:
    if type(item) == bs4.element.Tag:
        print "真正的兄弟节点：", item.name, item.attrs
