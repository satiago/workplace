#encoding:utf-8
'''
Created on 2014年11月28日

@author: yangsatiago
'''
#     ---------------------------------------  
#        程序：crawl_data  
#        版本：0.1
#        作者：satiago  
#        日期：2014-11-28  
#        语言：Python 2.7    
#        功能：数据库存储 
#     ---------------------------------------  
# 
import MySQLdb
import crawl_static
import sys

class Crawl_Data:
    
    def __init__(self):
        pass;
    
    def connect(self):
        try:
            self.conn = MySQLdb.connect(host = crawl_static.HOST, user = crawl_static.USER, passwd = crawl_static.PWD, db = crawl_static.DB, charset = crawl_static.CHARSET);
            self.cursor = self.conn.cursor();
        except:
            print "建立数据库连接失败！";
            self.close();
            return False;
        
        return True;

    def close(self):
        self.cursor.close();
        self.conn.close();
    
    def store_data(self, content):
        
        if content["source"] == "163":
            sql = "insert into tb_news_163 (news_date, news_time, news_title, news_source, news_text, news_link) values (%s,%s,%s,%s,%s,%s);";
        elif content["source"] == "tencent":
            sql = "insert into tb_news_qq (news_date, news_time, news_title, news_source, news_text, news_link) values (%s,%s,%s,%s,%s,%s);";
            
        param = (content["date"], content["time"], content["contents"]["title"], content["contents"]["source"], content["contents"]["text"], content["contents"]["link"]);
        
        try:
            self.cursor.execute(sql, param);
            self.conn.commit();
        except:
            print "保存数据失败";
            return False;
        
        return True;

    
if __name__ == '__main__':
    cd = Crawl_Data();
    result = cd.connect();
    
    if not result:
        sys.exit("退出！");
    
    content = {
               "source": "163",
               "date": "2014-02-04",
               "time": "08:08",
               "contents": {
                           "link": "http://www.baidu.com",
                           "title": "测试标题",
                           "source": "测试来源",
                           "text": "正文测试"
                           }
               };
    
    if cd.store_data(content):
        print "保存数据成功！";
        
    cd.close();
    
    
    