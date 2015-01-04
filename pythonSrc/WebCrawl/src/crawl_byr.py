# encoding: utf-8
'''
Created on 2014年11月26日

@author: yangsatiago
'''
import urllib2
from urllib2 import URLError
import httplib
import re
import cookielib
import urllib
import sys
import datetime

class byr_spider:
    
#     初始化
    def __init__(self):
        self.BYR_URL = "http://bbs.byr.cn";
        self.USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36";
        self.hot_pages_url = [];
        self.REG_TOPTEN = r"""<li\s*?class="widget color-default"\s*?id="topten">""";
        self.REG_TOPTEN_LIST = r"""<ul\s*?class="w-list-line">(.*?)</ul>""";
        self.REG_TOPTEN_CONTENT = r"""<li\s*?title="(.*?)">\s*?<a\s*?href="(.*?)">""";
        self.PWD = "ribeiyouhouqinbu";
        self.NAME = "satiago"; 
        
#         设置cookie和urlopen
        self.cookie = cookielib.CookieJar();
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie));
        
        #需要POST的数据#  
        self.postdata = urllib.urlencode({    
            'id':self.NAME,    
            'passwd':self.PWD,
            'mode':'0',
            'CookieDate':'3',      
        });
        
#     获取指定地址的网页内容
    def getHtmlContent(self, url):
        headers = {"User-Agent":self.USER_AGENT,
                "Referer": "http://bbs.byr.cn/",
                "Accept-Encoding": "gzip,deflate,sdch",
                "Accept-Language": "en-US,en;q=0.8",
                "Accept":"*/*",
                "X-Requested-With":"XMLHttpRequest"};
        req = urllib2.Request(url, headers = headers);
        
        try:
            response = self.opener.open(req);
            html = response.read();
            unicodehtml = html.decode("GBK").encode("utf-8");
        except URLError, e:
            print e;
            return "";
        except httplib.BadStatusLine, e:
            print "BadStatusLine error";
            return "";
        else:
#             print unicodehtml;
            return unicodehtml;
        
#     获取首页的内容   
    def getHomePage(self):
        
#         获取北邮人登录信息 
        try:
            headers = {"User-Agent":self.USER_AGENT,
                       "Referer":"http://bbs.byr.cn/index",
                       "Accept": "application/json, text/javascript, */*; q=0.01",
                       "X-Requested-With": "XMLHttpRequest"
                       };
            req = urllib2.Request("http://bbs.byr.cn/user/ajax_login.json", data = self.postdata, headers = headers);
            result = self.opener.open(req);

        except URLError, e:
            print e;
            login_byr = "";
        else:
            login_byr = result.read().decode("GBK").encode("utf-8");
#             print login_byr;

#         for item in self.cookie:
#             print "cookie.name=" + item.name + ";cookie.value=" + item.value;
        
        try:
            headers2 = {"User-Agent":self.USER_AGENT,
                "Referer": "http://bbs.byr.cn/",
                "Accept-Encoding": "gzip,deflate,sdch",
                "Accept-Language": "en-US,en;q=0.8",
                "Accept":"*/*",
                "X-Requested-With":"XMLHttpRequest"
                };
            
            req2 = urllib2.Request("http://bbs.byr.cn/user/ajax_session.json", headers=headers2);
            result2 = self.opener.open(req2);
        except URLError, e:
            print e;
            login2_byr = "";
        else:
            login2_byr = result2.read().decode("GBK").encode("utf-8");
#             print login2_byr;
           
#         获取首页内容 
        try:  
            req3 = urllib2.Request("http://bbs.byr.cn/default?_uid=satiago", headers=headers2);
            result3 = self.opener.open(req3);
        except URLError, e:
            print e;
            home_byr = "";
        else:
            home_byr = result3.read().decode("GBK").encode("utf-8");
#             print home_byr;
            
        return home_byr;
    
#     获取北邮人首页十大的链接
    def getHotPages(self):
        
        home = self.getHomePage();
        
        if home == "":
            print "获取首页内容失败";
            return [];
        
#         匹配topten的位置
        topten_pattern = re.compile(self.REG_TOPTEN, re.S);
        topten_match = topten_pattern.search(home);
        
        if topten_match:
#             print topten_match.group(0);
            pass;
        else:
            print "topten no match";
            return [];
        
 #         匹配toptenlist的内容       
        toptenlist_pattern = re.compile(self.REG_TOPTEN_LIST, re.S);
        toptenlist_match = toptenlist_pattern.search(home, pos=topten_match.end(0));
        
        if toptenlist_match:
#             print toptenlist_match.group(0);
#             print toptenlist_match.group(1);
            pass;
        else:
            print "toptenlist no match";
            return [];
        
#         提取toptenlist的内容和对应的链接       
        toptencontent_pattern = re.compile(self.REG_TOPTEN_CONTENT, re.S);
        toptencontent_match = toptencontent_pattern.findall(toptenlist_match.group(1));
        
        if toptencontent_match:
            for item in toptencontent_match:
#                 print "title:" + item[0] + "link:" + item[1];
                self.hot_pages_url.append({"title":item[0], "link":item[1]});  
        else:
            print "toptencontent no match";
            return [];
        
        return self.hot_pages_url;
    
    def getContent(self, listNum):
        html = self.getHtmlContent(self.BYR_URL + self.hot_pages_url[listNum]["link"] + "?_uid=satiago");
        
        pattern1 = re.compile(r"""<div class="a-u-uid">(.*?)</div>""");
        pattern2 = re.compile(r"""<dl class="a-u-info">(.*?)</dl>""");
        pattern3 = re.compile(r"""<dt>(.*?)</dt><dd>(.*?)</dd>""");
#         <dt>等级</dt><dd>用户</dd><dt>文章</dt><dd>71</dd><dt>积分</dt><dd>437</dd><dt>星座</dt><dd>白羊座</dd>
        
        position = 0;
        content = {};
        match1 = pattern1.search(html);
        
        if match1:
            author = match1.group(1);
            position = match1.end(0);
        else:
            position = 0;
            author = "无";
            
        content["作者"] = author;
        
        match2 = pattern2.search(html, pos=position);
        
        if match2:
            pass;
            position = match2.end(0);
        else:
            return content;
            
        match3 = pattern3.findall(match2.group(1));
        
        if match3:
            for item in match3:
                content[item[0]] = item[1];
        else:
            return content;
        
#         获取正文
        pattern4 = re.compile(r"""<div class="a-content-wrap">(.*?)<font class="f[0-9]{3}">※ 来源:·北邮人论坛 <a target="_blank" href="http://bbs.byr.cn">http://bbs.byr.cn</a>.*?</font>""");

        match4 = pattern4.search(html, pos=position);
        
        if match4:
#             print match4.group(0);
            article = match4.group(1);
            newarticle = article.replace("<br />", "\n").replace("&nbsp;", "");
            
            result, number = re.subn(r"""<.*?>""", "", newarticle);
            content["正文"] = result;
#             print result;
#             print number;
        else:
            content["正文"] = "无";
            return content;
        
        return content;
    
#     开始执行北邮人热点提取的程序
    def start(self):
        
        print "读取北邮人十大内容，请稍后^_^";
        topten = self.getHotPages();
        
        if topten == []:
            sys.exit("获取十大失败，程序退出！");
            
#         获取当前的时间
        dt = datetime.datetime.strftime(datetime.datetime.today(), "%d-%m-%y %H:%M");
        
        print u"""#---------------------------------------""";
        print u"#   北邮人论坛十大热门标题";
        print u"#   输入对应的编号进行浏览";
        print u"#   输入quit退出";
        print u"""#--------------------------------------- """;
        
        print "\n";
        print u"今天是:" + dt;
        print "\n";
        
        print u"""#--------------------------------------- """;
        for i in range(0, 10):
            print "#" + str(i) + " " + topten[i]["title"];
        print u"""#--------------------------------------- """;
        
#         等待用户输入
        while True:
#             user_input = raw_input("------->");
            user_input = raw_input("------->");
#             print type(user_input);
            if user_input == "":
                print "请输入编号或者quit退出";
                continue;
            
            if user_input == "quit":
                sys.exit("bye");
            elif '0' <= user_input <= '9':
    #                     print user_input;
                info = self.getContent(int(user_input));
    #                     for item in info.items():
    #                         print item[0];
    #                         print item[1];
    #                     for key in info.keys():
    #                         print "%s:%s" % (key, info[key]); 
                print u"""#--------------------作者信息---------------- """;
                if not info.has_key("作者"):
                    info["作者"] = "无";
                if not info.has_key("等级"):
                    info["等级"] = "无";
                if not info.has_key("积分"):
                    info["积分"] = "无";
                if not info.has_key("文章"):
                    info["文章"] = "无";
                if not info.has_key("星座"):
                    info["星座"] = "无";
                print "作者：" + info["作者"];
                print "等级：" + info["等级"];
                print "积分：" + info["积分"];
                print "文章：" + info["文章"];
                print "星座：" + info["星座"];
                print u"""#--------------------------------------- """;
                print info["正文"];
                print u"""#--------------------------------------- """;  
            else:
                print "不要闹了,亲^_^";
                    
            
                    
if __name__ == '__main__':
    #-------- 程序入口处 ------------------  
    print u"""#--------------------------------------- 
    #   程序：北邮人论坛十大热门内容 
    #   版本：0.1
    #   作者：satiago 
    #   日期：2014-11-26 
    #   语言：Python 2.7 
    #--------------------------------------- 
    """;
    
    bs = byr_spider();
    bs.start();

    

    
    
    
    
    