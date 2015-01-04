#encoding:utf-8
'''
Created on 2014年11月28日

@author: yangsatiago
'''
#     ---------------------------------------  
#        程序：crawl_dispatch  
#        版本：0.1
#        作者：satiago  
#        日期：2014-11-28  
#        语言：Python 2.7    
#        功能：分发链接内容到指定的分析引擎  
#     ---------------------------------------  
# 
import crawl_static
import re
import crawl_sina
from crawl_static import TYPE_163, TYPE_TENCENT, TYPE_SINA, TYPE_NO
from crawl_163 import Crawl_163
from crawl_tencent import Crawl_qq

class Crawl_Dispatch:
    
    def __init__(self):
        pass;
    
    def dispatch_url(self, url):
        
#         判断URL的类型
        if self.dispatch_type(url, crawl_static.REG_SINA_HTTP):
            print "新浪页面";
            return TYPE_SINA;
        elif self.dispatch_type(url, crawl_static.REG_163_HTTP):
            print "网易页面";
            return TYPE_163;
        elif self.dispatch_type(url, crawl_static.REG_TENCENT_HTTP):
            print "腾讯页面";
            return TYPE_TENCENT;
        else:
            print "不匹配任何类型页面";
            return TYPE_NO;
            
    def dispatch_type(self, url, reg):
        pattern = re.compile(reg);
        match = pattern.match(url);
        
        if match:
            return True;
        else:
            return False;
    
    def dispatch_engine(self, type, url):
        if type == TYPE_SINA:
            print "新浪页面";
        elif type == TYPE_163:
#             print "网易页面";
            cw = Crawl_163();
            cw.start(url);
        elif type == TYPE_TENCENT:
#             print "腾讯页面";
            cq = Crawl_qq();
            cq.start(url);

    
if __name__ == '__main__':
    pass