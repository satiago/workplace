# encoding: utf-8
'''
Created on 2014年11月28日

@author: yangsatiago
'''
#     ---------------------------------------  
#        程序：crawl_163 
#        版本：0.1
#        作者：satiago  
#        日期：2014-11-28  
#        语言：Python 2.7    
#        功能：提取指定网易页面的新闻内容  
#     ---------------------------------------  
#   

from bs4 import BeautifulSoup
import crawl_static
import urllib2
from urllib2 import URLError
import httplib
import re
import sys
from crawl_data import Crawl_Data

class Crawl_163:
    
    def __init__(self):
        self.page = "";
    
    def start(self, url):
#         获取网易页面
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
            print "保存网易新闻数据成功！";
            
        cd.close();
            
#         分析抓取到的内容，提取信息
    def getHtmlContent(self, page):
        content = crawl_static.CONTENT_163;
        soup = BeautifulSoup(page);
#         print soup.original_encoding;
#         print(soup.prettify());
        
#         获取网易新闻的正文部分
        content1 = soup.find("div", id="epContentLeft");
#         标题
        if content1:
            content2 = content1.find("h1", id="h1title");
            if content2:
                content["contents"]["title"] = content2.get_text();
            else:
                content["contents"]["title"] = "无";
        else:
            print "获取正文失败！";
            return {};
            
#         来源
        content3 = content1.find("div", class_="ep-time-soure cDGray");
        
        if content3:
            date_source = content3.get_text();
            
#             匹配字符串中的日期和来源
            pattern = re.compile(crawl_static.REG_SOURCE);
            match = pattern.search(date_source);
            
            if match:
#                 print match.group(1);
#                 print match.group(2);
                str_source = match.group(3).replace(" ", "");
                str_ssource = str_source.replace(u"来源:", "");
#                 print str;
                
                content["contents"]["source"] = str_ssource;
                content["date"] = match.group(1);
                content["time"] = match.group(2);
                
            else:
                print "未匹配";
        else:
            content["contents"]["source"] = "无";
            content["date"] = "无";
            content["time"] = "无";
            
#         获取正文内容
        content4 = content1.find_all("div", id="endText");
        html_content = "";
        if content4:
            for item in content4:
                for tag in item.find_all("p"):
                    if tag.find("style"):
                        continue;
                    html_content += tag.get_text() + "\n";
#                 print tag.get_text();
#             print html_content;
            content["contents"]["text"] = html_content;
            content["contents"]["link"] = self.page;
        else:
            content["contents"]["text"] = "无";
            content["contents"]["link"] = self.page;
        
        return content;
        
if __name__ == '__main__':
    cw = Crawl_163();
    cw.start("http://news.163.com/14/1204/02/ACJAUOQC00014AED.html");