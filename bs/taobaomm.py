# -*- coding:UTF-8 -*-
########################
#
# Created on 2015-05-02
# @author: zhenfei.wang

# 通过URL地址：http://mm.taobao.com/json/request_top_list.htm?page=1 抓取淘宝平面模特的基本资料
########################

import urllib2
import tool
import bs4
from bs4 import BeautifulSoup


class Taobao:
    def __init__(self):
        self.url = "http://mm.taobao.com/json/request_top_list.htm"
        self.tool = tool.Tool()

    def getPageContent(self, page_no):
        req_url = self.url + "?page=" + str(page_no)
        req = urllib2.Request(req_url)
        resp = urllib2.urlopen(req)
        # 此页面无法用UTF-8 decode
        return resp.read().decode('gbk')


    def getAllDesc(self, soup_content):
        # 由于class是关键词，所以这里要写成class_
        for item in soup_content.find_all("p", class_="description"):
            print self.tool.replace(item.string)

    def getAllName(self, soup_content):
        for item in soup_content.find_all("p", class_="top"):
            print item.a.string

    def getAll(self, soup_content):

        mmNo = 1

        for mmItem in soup_content.find_all("div", class_="list-item"):
            print "淘女郎 NO." + str(mmNo), " -----> "
            print "姓名：", mmItem.div.div.p.a.string
            print "年龄：", mmItem.div.div.p.em.strong.string
            print "城市：", mmItem.div.div.p.span.string


            # 由于标签的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
            # 而空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行，所以用这两个方法有问题，需要改善

            for child in mmItem.div.div.p.next_siblings:
                if child.name and type(child) == bs4.element.Tag and str(child.name) == 'p':
                    print "职位：", child.em.string

            for child in mmItem.div.next_siblings:
                if child.name and type(child) == bs4.element.Tag and str(child.name) == 'div':
                    print "desc：", tool.Tool().replace(child.p.string)

            print "头像：", mmItem.div.div.div.a.img.attrs['src']

            print "###############################"
            mmNo += 1


taobao = Taobao()
page_no = 1
soup = BeautifulSoup(taobao.getPageContent(page_no))
print soup.prettify()

print "###################"

taobao = Taobao()
# taobao.getDesc(soup)
# taobao.geName(soup)
# taobao.getAge(soup)

taobao.getAll(soup)