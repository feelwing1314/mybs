__author__ = 'afei'
# -*- coding:UTF-8 -*-
# Created On : 2015-05-02
# Author: zhenfei.wang
# 本次抓取地址：

# 重要知识点：
# Cookie的使用，模拟登录的功能。
#
#######################

import urllib
import urllib2
import cookielib
import simplejson as json
import re


class Zealer:
    def __init__(self):
        self.loginUrl = "http://www.zealer.com/login/login"
        self.infoUrl = "http://www.zealer.com/user?type=info"
        self.myCommentUrl = "http://www.zealer.com/user?type=mycom"

        # CookieJar这个对象会保存登陆后的cookies信息
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            "username": "404961061@qq.com",
            "password": "13875674621"
        })
        # 通过构建opener，利用open方法实现了登录
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPageContent(self):

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}

        req = urllib2.Request(url=self.loginUrl, data=self.postdata, headers=headers)
        resp = self.opener.open(req)
        json_str = resp.read().decode("UTF-8")
        print json_str

        req = urllib2.Request(url=self.myCommentUrl, headers=headers)
        result = self.opener.open(req)
        return result.read().decode("UTF-8")



zealer = Zealer()
content = zealer.getPageContent()
print content

# 打印cookie信息
for item in zealer.cookies:
    print 'Cookie：Name = '+item.name, ', Value = '+item.value