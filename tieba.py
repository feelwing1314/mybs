########################
# -*- coding:UTF-8 -*-
# Created On : 2015-05-02
# Author: zhenfei.wang
# 本次抓取贴吧的URL地址：http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

# 重要知识点：
# pattern = re.compile('<h1.*?class="core_title_txt.*?".*?>(.*?)</h1>', re.S)
# re.search(pattern, page_content)
# result.group(1).strip()
#
########################


import urllib2
import re

class Tieba:
    def __init__(self, baseUrl, seeLz):
        self.baseUrl = baseUrl
        self.seeLz = '?see_lz='+str(seeLz)


    def getPageContent(self, page_no):
        try:
            url = self.baseUrl+self.seeLz+"&pn="+str(page_no)
            req = urllib2.Request(url)
            resp = urllib2.urlopen(req, None, 1000)
            return resp
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败, 错误原因: ",e.reason
                return None

    def getTitle(self, page_content):

        html = """
                <div class="core_title core_title_theme_bright"><h1 class="core_title_txt  "
                                                                                                title="纯原创我心中的NBA2014-2015赛季现役50大"
                                                                                                style="width: 396px">
                                                纯原创我心中的NBA2014-2015赛季现役50大</h1>
                                                <ul class="core_title_btns">
                                                    <li><a id="lzonly_cntn" href="/p/3138733512" alog-alias="lzonly"
                                                           class="l_lzonly_cancel"><span id="lzonly"
                                                                                         class="d_lzonly_bdaside">取消只看楼主</span></a></li>
                                                    <li id="j_favthread" class="p_favthread"
                                                        data-field='{&quot;status&quot;:0,&quot;is_anonym&quot;:false}'>
                                                        <div class="p_favthr_tip"></div>
                                                        <div class="p_favthr_main"><p>收藏</p></div>
                                                    </li>
                                                    <li class="quick_reply"><a href="#" id="quick_reply" class="j_quick_reply">回复</a>
                                                    </li>
                                                </ul>
                                            </div>

                                            '<div.*?class="core_title.*?".*?>.*?<h1.*?class="core_title_txt.*?".*?>(.*?)</h1>.*?</div>'
                """

        pattern = re.compile('<div.*?class="core_title.*?".*?>.*?'
                             '<h1.*?class="core_title_txt.*?".*?>(.*?)</h1>.*?'
                             '</div>', re.S)
        result = re.search(pattern, page_content)
        if result:
            # print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            return None


    def getTotalPageNo(self, page_content):
        html = """
        <li class="l_reply_num" style="margin-left:8px">
                                    <span class="red" style="margin-right:3px">138</span>
                                    回复贴，共
                                    <span class="red">5</span>页
                                </li>
        """
        pattern = re.compile('<div.*?class="pb_footer".*?>.*?'
                             '<li.*?class="l_reply_num.*?>.*?'
                             '<span.*?>.*?</span>.*?'
                             '<span.*?>(.*?)</span>.*?</li>', re.S)
        result = re.search(pattern, page_content)
        if result:
            return result.group(1).strip()
        else:
            return None


    def getPostContent(self, page_content):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        # pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page_content)
        for item in items:
            if not item[0]:
                print item[0]

baseUrl = "http://tieba.baidu.com/p/3138733512"
spiderTieba = Tieba(baseUrl, 1)
content = spiderTieba.getPageContent(1).read().decode('utf-8')

print content

print "##########################"


print "贴吧标题  :", spiderTieba.getTitle(content)
print "贴吧总页数:", spiderTieba.getTotalPageNo(content)

print "TOP50 :",    spiderTieba.getPostContent(content)