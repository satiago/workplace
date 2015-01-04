# encoding: utf-8
'''
Created on 2014年11月25日

@author: yangsatiago
'''
import urllib2
import sys
import httplib
import re
import thread
import time
from urllib2 import URLError

def getDebugInfo():
    try:
        raise Exception;
    except:
        f = sys.exc_info()[2].tb_frame.f_back;
        return "problem in file %s, in function %s, at line %s" % (f.f_code.co_filename, f.f_code.co_name, f.f_lineno);
    
class Spider_Model:
    
    def __init__(self):
        self.page = 1;
        self.pages = [];
        self.enable = False;
        
    def getPage(self, page):
        items = [];
        url = "http://m.qiushibaike.com/hot/page/" + str(page);
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36";
        headers = {"User-Agent":user_agent};
        req = urllib2.Request(url, headers = headers);
        
        try:
            response = urllib2.urlopen(req);
            html = response.read();
            unicodehtml = html.decode("utf-8").encode("utf-8");
#             print unicodehtml;
        except URLError, e:
            print e;
            return [];
        except httplib.BadStatusLine, e:
            print "BadStatusLine error";
            return [];
        
        first_pattern = re.compile(r"""<div class="article block untagged mb15" id=['"]qiushi_tag_[0-9]{8}['"]>""", re.S);
        second_pattern = re.compile(r"""<div class="author clearfix">\s*?<a href="/users/[0-9]{7,}">\s*?<img src="http://.*?" alt="(.*?)"\s?/>""", re.S);
        third_pattern = re.compile(r"""<div class="content" title="(.*?)">(.*?)</div>""", re.S);
        
        position = 0;
        
        while position < len(unicodehtml):
            first_match = first_pattern.search(unicodehtml, pos=position);
            
            if first_match:
                position = first_match.end(0);
#                 print first_match.group(0);
#                 print first_match.span(0);
            else:
#                 print "first no match";
                break;
            
            second_match = second_pattern.search(unicodehtml, pos=position);
            
            if second_match:
                position = second_match.end(0);
                author = second_match.group(1);
#                 print second_match.group(0);
#                 print second_match.group(1);
#                 print second_match.span(0);
            else:
                print "second_no_match";
                author = "无";
    
            third_match = third_pattern.search(unicodehtml, pos=position);
            
            if third_match:
                position = third_match.end(0);
                time = third_match.group(1);
                content = third_match.group(2);
#                 print third_match.group(0);
#                 print third_match.group(1);
#                 print third_match.group(2);
#                 print third_match.span(0);
            else:
                print "third_no_match";
                time = u"无";
                content = u"无";
            
            items.append([author, time, content]);
        
        return items;
    
    def loadPage(self):
                # 如果用户未输入quit则一直运行    
        while self.enable:    
            # 如果pages数组中的内容小于2个    
            if len(self.pages) < 2:    
                try:    
                    # 获取新的页面中的段子们    
                    myPage = self.getPage(str(self.page));    
                    self.page += 1;    
                    self.pages.append(myPage);    
                except:    
                    print '无法链接糗事百科！'; 
#                     thread.exit();
                    
                    
            else:    
                time.sleep(1);
    
    def showPage(self, nowPageContent, page):
        for item in nowPageContent:
            print "页数：%s" % page;
            print "时间：" + item[1];
            print "作者：" + item[0];
            print "内容：" + item[2];
            
        userInput = raw_input("--->");
        
        if userInput == "quit":
            self.enable = False;
        
    
    def start(self):
        self.enable = True;
        page = self.page;
        
        print u'正在加载中请稍候......';
        
        thread.start_new_thread(self.loadPage,());
        
                #----------- 加载处理糗事百科 -----------    
        while self.enable:    
            # 如果self的page数组中存有元素    
            if self.pages:    
                nowPageContent = self.pages[0];    
                del self.pages[0];    
                self.showPage(nowPageContent, page);    
                page += 1; 
            
            
        
if __name__ == '__main__':
    
    #----------- 程序的入口处 -----------    
    print u"""  
    ---------------------------------------  
       程序：糗百热点内容抓取  
       版本：0.1
       作者：satiago  
       日期：2014-11-25  
       语言：Python 2.7  
       操作：输入quit退出阅读糗事百科  
       功能：按下回车依次浏览今日的糗百热点  
    ---------------------------------------  
    """  
    raw_input("--->请点击回车浏览");
    
    sm = Spider_Model();
    sm.start();
    