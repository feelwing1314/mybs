# -*- coding:UTF-8 -*-
########################
#
# Created on 2015-05-02
# @author: zhenfei.wang

# 通过URL地址：http://mm.taobao.com/json/request_top_list.htm?page=1 抓取淘宝平面模特的基本资料
########################

import urllib2
import re
import tool

class Taobao:
    def __init__(self):
        self.url = "http://mm.taobao.com/json/request_top_list.htm"
        self.tool = tool.Tool()

    def getPageContent(self, page_no):
        req_url = self.url+"?page="+str(page_no)
        req = urllib2.Request(req_url)
        resp = urllib2.urlopen(req)
        # 此页面无法用UTF-8 decode
        return resp.read().decode('gbk')

    def getBasicInfo(self, content, curr_page_no):

        pattern = re.compile('<div.*?class="list-item">.*?'
                             '<div.*?class="personal-info">.*?'
                             '<div.*?class="pic.*?">.*?<a.*?src="(.*?)".*?>.*?</a>.*?'
                             '<p.*?class="top">.*?<a class="lady-name".*?>(.*?)</a>.*?'
                             '<em>.*?<strong>(.*?)</strong>.*?</em>.*?'
                             '<span>(.*?)</span>.*?'
                             '<p>.*?<em>(.*?)</em>.*?<em>.*?<strong>.*?</strong>.*?</em>.*?</p>.*?'
                             '<div.*?class="list-info">.*?'
                             '<p.*?class="description">(.*?)</p>', re.S)
        # 淘女郎编号
        mmNo = 1

        for mmItem in re.findall(pattern, content):
            print "NO."+str(mmNo+(curr_page_no-1)*10), "###############################"
            print "姓名：", mmItem[1]
            print "年龄：", mmItem[2]
            print "城市：", mmItem[3]
            print "职业：", mmItem[4]
            print "desc：", self.tool.replace(mmItem[5])
            print "头像：", mmItem[0]
            print "###############################"
            mmNo += 1

taobao = Taobao()
for page_no in [1, 2, 3]:

    taobao.getBasicInfo(taobao.getPageContent(page_no), page_no)