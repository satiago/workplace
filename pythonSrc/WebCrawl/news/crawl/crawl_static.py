#encoding:utf-8
'''
Created on 2014年12月1日

@author: yangsatiago
'''
# 正则表达式
REG_SINA_HTTP = r"""^http://[\w+]{1,}?.sina.com.cn/.*?$""";
REG_163_HTTP = r"""^http://[\w+]{1,}?.163.com/.*?$"""; 
REG_TENCENT_HTTP = r"""^http://[\w+]{1,}?.qq.com/.*?$""";

TYPE_NO = 0;
# 新浪
SINA_URL = "http://news.sina.com.cn/";
SINA_DOMAIN = "sina.com.cn";
TYPE_SINA = 1;

# 网易
REG_SOURCE = r"""(\d{4}-\d{2}-\d{2})\s*?(\d{2}:\d{2}:\d{2})\s*?(.*)""";
URL_163 = "http://www.163.com/";
DOMAIN_163 = "163.com";
TYPE_163 = 2;

# 腾讯
REG_DATE = r"""(\d{4}-\d{2}-\d{2})\s*?(\d{2}:\d{2})""";
TENCENT_URL = "http://www.qq.com/";
TENCENT_DOMAIN = "qq.com";
TYPE_TENCENT = 3;

# 数据库信息
HOST = "127.0.0.1";
USER = "root";
PWD = "12345";
DB = "db_news";
CHARSET = "utf8";

# 数据存储格式
CONTENT_163 = {
               "source": "163",
               "date": "",
               "time": "",
               "contents": {
                           "link": "",
                           "title": "",
                           "source": "",
                           "text": ""
                           }
               };
               
CONTENT_QQ = {
               "source": "tencent",
               "date": "",
               "time": "",
               "contents": {
                           "link": "",
                           "title": "",
                           "source": "",
                           "text": ""
                           }
               };
