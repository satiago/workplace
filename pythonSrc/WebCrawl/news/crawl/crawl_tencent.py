#encoding:utf-8
'''
Created on 2014年11月28日

@author: yangsatiago
'''
#     ---------------------------------------  
#        程序：crawl_tencent  
#        版本：0.1
#        作者：satiago  
#        日期：2014-11-28  
#        语言：Python 2.7    
#        功能：提取指定腾讯页面的新闻内容  
#     ---------------------------------------  
# 
import urllib2
from urllib2 import URLError
import httplib
import crawl_static
from bs4 import BeautifulSoup
import re
import sys
from crawl_data import Crawl_Data

class Crawl_qq:
    def __init__(self):
        self.page = "";
        
    def start(self, url):
#         获取腾讯页面
        self.page = url;
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36";
        headers = {"User-Agent":user_agent};
        req = urllib2.Request(url, headers = headers);
        
        try:
            response = urllib2.urlopen(req);
            html = response.read();
        except URLError, e:
            print e;
            html = "";
        except httplib.BadStatusLine, e:
            print "BadStatusLine error";
            html = "";
        
        if html:
            content = self.getHtmlContent(html);
        else:
            content = {};
        
        if not content:
            sys.exit("未提取到新闻信息！");
        
        print content["source"];
        print content["date"];
        print content["time"];
        print content["contents"]["link"];
        print content["contents"]["title"];
        print content["contents"]["source"];
        print content["contents"]["text"]; 
  
#         将提取到的数据存到数据库中      
        cd = Crawl_Data();
        result = cd.connect();
    
        if not result:
            sys.exit("退出！");
        
        if cd.store_data(content):
            print "保存腾讯新闻数据成功！";
            
        cd.close();   
            
#         分析抓取到的内容，提取信息
    def getHtmlContent(self, page):
        content = crawl_static.CONTENT_QQ;
        soup = BeautifulSoup(page, "html5lib");
#         print soup.original_encoding;
#         print(soup.prettify());
        
#         获取腾讯新闻的正文信息
        content1 = soup.find("div", id="C-Main-Article-QQ");
        
        if content1:
            content_info = content1.find("div", class_="hd");
        else:
            print "未获取腾讯新闻的正文信息！";
            return {};
        
#         获取腾讯新闻的标题等信息
        if content_info:
            titleTag = content_info.find("h1");
            if titleTag: 
                title = titleTag.get_text();
            else:
                title = "无";
            
#             print title;
            content["contents"]["title"] = title;
            
            sourceTag = content_info.find("span", class_="color-a-1", bosszone="jgname");
            if sourceTag:
                source = sourceTag.get_text();
            else:
                source = "无";
                
#             print source;
            content["contents"]["source"] = source;
                
            dateTag = content_info.find("span", class_="article-time");
            if dateTag:
                date = dateTag.get_text();                    
            else:
                date = "无";
            
            pattern = re.compile(crawl_static.REG_DATE);
            match = pattern.search(date);
                
            if match:
#                 print match.group(1);
#                 print match.group(2);
                content["date"] = match.group(1);
                content["time"] = match.group(2);
            else:
                content["date"] = "无";
                content["time"] = "无";
            
#             获取正文
            text = "";
            content_qq = content1.find("div", id="Cnt-Main-Article-QQ", bosszone="content");
            if content_qq:
                content_text = content_qq.find_all("p");
                for item in content_text:
                    if item.find("style"):
                        continue;
                    text += item.get_text() + "\n";
            else:
                text = "无";
            
#             print text;
            content["contents"]["text"] = text;
            content["contents"]["link"] = self.page;
            
            return content;
                      
if __name__ == '__main__':
    cq = Crawl_qq();
    cq.start("http://news.qq.com/a/20141202/027934.htm");
    