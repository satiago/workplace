#encoding:utf-8
'''
Created on 2014年11月28日

@author: yangsatiago
'''
#     ---------------------------------------  
#        程序：crawl_main  
#        版本：0.1
#        作者：satiago  
#        日期：2014-11-28  
#        语言：Python 2.7    
#        功能：提取指定页面的新闻内容  
#     ---------------------------------------  
# 
import sys
import crawl_dispatch
import crawl_static
    
if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        sys.exit("usage:" + sys.argv[0] + " " + "http://news-url");
        
#     获取用户输入的url地址
    url = sys.argv[1];
    
#     分析url地址，交给对应的分析引擎
    cd = crawl_dispatch.Crawl_Dispatch();
    type = cd.dispatch_url(url);
    
    if type == crawl_static.TYPE_NO:
        sys.exit("输入的URL地址无法匹配，退出！");
    else:
        cd.dispatch_engine(type, url);
    
    
    
    
    
    
    