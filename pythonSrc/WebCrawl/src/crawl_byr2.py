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

class byr_spider:
    
#     初始化
    def __init__(self):
        self.BYR_URL = "http://bbs.byr.cn/";
        self.USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36";
        self.hot_pages_url = [];
        self.REG_TOPTEN = r"""<li\s*?class="widget color-default"\s*?id="topten">""";
        self.REG_TOPTEN_LIST = r"""<ul\s*?class="w-list-line">(.*?)</ul>""";
        self.PWD = "ribeiyouhouqinbu";
        self.NAME = "satiago"; 
        
        #需要POST的数据#  
        self.postdata = urllib.urlencode({    
            'id':self.NAME,    
            'passwd':self.PWD,
            'mode':'0',
            'CookieDate':'3',      
        });
        
#         建立初始http连接
        try:
            self.conn = httplib.HTTPConnection("bbs.byr.cn");
        except httplib.HTTPException, e:
            print e;
            print "初始化http连接失败，退出！";
            self.conn = "failed";
            
        
#     获取指定地址的网页内容
#     def getHtmlContent(self, url):
#         headers = {"User-Agent":self.USER_AGENT};
#         req = urllib2.Request(url, headers = headers);
#         
#         try:
#             response = self.opener.open(req);
#             html = response.read();
#             unicodehtml = html.decode("GBK").encode("utf-8");
#         except URLError, e:
#             print e;
#             return "";
#         except httplib.BadStatusLine, e:
#             print "BadStatusLine error";
#             return "";
#         else:
#             print unicodehtml;
#             return unicodehtml;
        
#     获取首页的十大热点链接    
    def getHotPages(self):
        
#         获取北邮人的登录信息
        try:
            headers = {"User-Agent":self.USER_AGENT,
                       "Referer":"http://bbs.byr.cn/index",
                       "Accept": "application/json, text/javascript, */*; q=0.01",
                       "X-Requested-With": "XMLHttpRequest",
                       "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
                       };
            
            self.conn.request("POST", "/user/ajax_login.json", self.postdata, headers);
            response = self.conn.getresponse();
            cookie = response.getheader("Set-Cookie");
        except httplib.HTTPException, e:
            print e;
            login_byr = "";
            self.conn.close();
        else:
            login_byr = response.read().decode("GBK").encode("utf-8");
            print login_byr;
            
            
        
#         获取北邮人的首页内容
        try:
            headers2 = {"User-Agent":self.USER_AGENT,
                "Referer": "http://bbs.byr.cn/",
                "Accept-Encoding": "gzip,deflate,sdch",
                "Accept-Language": "en-US,en;q=0.8",
                "Accept":"*/*",
                "X-Requested-With":"XMLHttpRequest",
                "Cookie":cookie
                };
            
            self.conn.request("GET", "/user/ajax_session.json", headers=headers2);
            response2 = self.conn.getresponse();
        except httplib.HTTPException, e:
            print e;
            home_byr = "";
            self.conn.close();
        else:
            home_byr = response2.read().decode("GBK").encode("utf-8");
            print home_byr;
        
                      
if __name__ == '__main__':
    #-------- 程序入口处 ------------------  
    print u"""#--------------------------------------- 
    #   程序：北邮人论坛十大热门内容 
    #   版本：0.1
    #   作者：satiago 
    #   日期：2014-11-26 
    #   语言：Python 2.7 
    #   操作：暂无 
    #   功能：暂无
    #--------------------------------------- 
    """;
    
    bs = byr_spider();
    
    if bs.conn == "failed":
        sys.exit("程序退出");
        
    bs.getHotPages();
    

    
    
    
    
    