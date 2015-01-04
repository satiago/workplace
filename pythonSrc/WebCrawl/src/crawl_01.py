#coding:utf-8
# '''
# Created on 2014年11月24日
# @author: yangsatiago
# '''

import urllib2
import cookielib
import re
from urllib2 import URLError, HTTPError

if __name__ == '__main__':
#     soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
#     tag = soup.b
#     print tag.name
# 重定向网址和原网址的比对
#     my_url = 'http://www.baidu.com'  
#     response = urllib2.urlopen(my_url)  
#     redirected = response.geturl() == my_url  
#     print redirected
    
#     获取cookie值
#     cookie = cookielib.CookieJar()  
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
#     response = opener.open('http://www.baidu.com')  
#     for item in cookie:  
#         print 'Name = '+item.name  
#         print 'Value = '+item.value
        
#         异常处理
#     try:
#         req = urllib2.Request("http://192.168.113.1");
#         response = urllib2.urlopen(req);
#     except HTTPError, e:
#         print e.reason;
#         print e.code;
#     except URLError, e:
#         print e.reason;
#     else:
#         html = response.read();
#         print response.info();
# #         print html;
#     finally:
#         print "call finally";
        
    pattern = re.compile(r"""(.*?):交换:(.+)""");
     
    match1 = pattern.search("""甲方:交换:甲方""");
     
    if match1:
        print match1.group(0);
        print match1.group(1);
        print match1.group(2);
    else:
        print "未匹配到";
        
        
    