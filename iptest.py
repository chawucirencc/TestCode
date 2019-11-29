import re
import sys
import time
import pymysql
import pyspider
import requests
from tkinter import *
from lxml import etree
from selenium import webdriver
from pyquery import PyQuery as pq
from matplotlib import pyplot as plt
import tkinter.messagebox as messagebox


class GetIPinfo:
    """
    IP测试类，使用请求，同时使用xpath提取信息！
    """
    def __init__(self, url):
        self.url = url
        
    def getstatus(self):
        try:
            res = requests.get(self.url)
            res.status_code == 200
            res.encoding = "utf-8"
            # print(res.text)
            # print(type(res.text))
            return res.text
        except Exception as err:
            print(err)
        
    def getpageinfo_etree(self):
        """
        使用lxml的etree解析。
        """
        page = etree.HTML(self.getstatus())
        response = page.xpath(".//div[@class='data kq-well']//pre//text()")
        # print(response)
        try:
            result = re.sub("/n", " ", response[0])
            print(result)
        except Exception as err:
            print(err)
            
            
class UseQuerymodel(GetIPinfo):
    def sendRequest(self):
        """
        使用pyquery请求解析网页，使用基于CSS的选择器选取数据。发送请求的这个方法可以调用父类的requests请求方法。
        """
        response = pq(self.url, encoding='utf-8')
        print(type(response))
        print(response)
        # print(response)
        
    
    def parseHtml(self):
        """
        使用pyquery对网页进行解析。
        """
        response = pq(self.getstatus())
        print(type(response))
        print(response)
        
        
def processpageinfo(url):
    """
    对一个功能编写成类，然后接下来使用一个访哈实例化这个类，最后在main函数中执行就行了。唯一的缺点就是在多个函数中调用。
    """
    # print("/----------------------------/")
    # ip = input("Test IP address：")
    # print("/----------------------------/")
    # ip = input("输入IP:")
    # url = "http://www.cip.cc/"+ip
    page = UseQuerymodel(url)
    page.parseHtml()
    


class OpenPage:
    """
    测试selenium
    """
    def openwebpage(self):
        browser = webdriver.Chrome()
        browser.get('https://www.baidu.com/')
    
    def inserttext(self):
        s = "This is test text!"
        return s
    
           
class Application(Frame, OpenPage):
    """
    GUI编程测试，简单窗口按键方法测试
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text="Hello window")
        self.helloLabel.pack()
        self.openchromebutton = Button(self, text="OpenChrome", command=self.openwebpage) # 打开浏览器按钮
        self.openchromebutton.pack(padx=10)
        self.quitbutton = Button(self, text="quit", command=self.quit)
        self.quitbutton.pack(side=LEFT, padx=50)
        
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.comfirmbutton = Button(self, text="确定", command=self.gettext)
        self.comfirmbutton.pack(side=RIGHT)
        
        self.inserttext = Text(self)
        
    def gettext(self):
        name = self.nameInput.get()
        messagebox.showinfo("Title", name)
    
    
def opwindow():
    """
    GUI测试...
    """
    app = Application()
    app.master.title("window")
    app.master.geometry("1200x800")
    app.mainloop()


class GetNumber(GetIPinfo):
    def __init__(self, url):
        self.url = url
        
    def get_pagestatus(self):
        """
        测试重写方法，暂时不用此方法！
        """
        try:
            r = requests.get(self.url)
            print(r.status_code)
            r.status_code == 200
            r.encoding = "utf-8"
            print(r.text)
            return r.text
        except Exception as err:
            print(err)
    
    def process_pageinfo(self):
        """
        使用切片切分列表，
        """
        res = etree.HTML(super().getstatus())
        number = res.xpath(".//em/text()")
        # print(number)
        # print(len(number))
        small_list = []
        for i in range(0, len(number), 7):
            small_list.append(number[i:i+7])
        return small_list
    
    def connection_sql(self):
        """
        连接数据库，将得到的数据写入到MySQL中。
        """
        a = 0
        for i in self.process_pageinfo():
            # print(i)
            if i not in self.select_data():
                db = pymysql.connect(host="localhost", user="root", password="password", database="world")
                db_curs = db.cursor()
                insert_sql = """INSERT INTO number(A, B, C, D, E, F, G) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                data = [i] 
                # print(data)
                try:
                    db_curs.executemany(insert_sql, data)
                    db.commit()
                    print("OK", i)
                except Exception as err:
                    db.rollback()
                    print("insert error", err)    
            else:
                print("已存在", i)
                a += 1
                if a == 3:
                    break
                continue  
            db_curs.close()
            
    def select_data(self):
        """
        查询所有数据，可以将其转化成list。
        关于使用SQL更新数据的方法，在下面的方法中就是将所有的的数据添加到一个列表当中，然后判断新得到的是否在这个列表当中，如果存在那么就跳过，
        如果不存在那就添加到数据库中。随着数据量的增加，列表的占用空间也会越来越大，性能消耗会比较严重。每次判断都会进行MySQL的查询。
        """
        db = pymysql.connect(host="localhost", user="root", password="password", database="world")
        db_curs = db.cursor()
        select_all = "select * from number;"
        db_curs.execute(select_all)
        result = db_curs.fetchall()
        result_lsit = [] # 将所有数据存到列表中有20k的大小。
        for i in result:
            result_lsit.append(list(i[1:]))
        return result_lsit    
        
        
def use_getnumber():
    """
    在需要更新数据的时候运行程序，只会显示OK和已存在两种情况，如果连续三页的前三个都是已存在的状态，则说明没有数据需要更新了，那么就退出程序。
    """
    s = 0
    for i in range(1, 126):
        s += 1
        if s < 4:
            print("第{0}页前三项".format(s))
            url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_"+str(i)+".html"
            an = GetNumber(url)
            an.connection_sql()
            time.sleep(2)
        else:
            break
        

class ConnectionSql():
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        
    def select_data(self):
      pass
    

class AnalysisNumber():
    def __init__(self):
        pass
    
    def select_data(self):
        """
        查询所有数据，可以将其转化成list。
        """
        db = pymysql.connect(host="localhost", user="root", password="password", database="world")
        db_curs = db.cursor()
        select_sql = "SELECT G, COUNT(*) as 总计 FROM number GROUP BY G ORDER BY COUNT(*) DESC;"
        select_sql_1 = """SELECT `序号` FROM number WHERE A = 4 AND B = 6 AND C = 11 AND D = 14 AND E = 19 AND F = 33 AND G = 7 
                LIMIT 1;"""
        select_all = "select * from number;"
        db_curs.execute(select_all)
        result = db_curs.fetchall()
        result_lsit = [] # 将所有数据存到列表中有20k的大小。
        for i in result:
            result_lsit.append(list(i[1:]))
        # print(result)
        # print(len(result))
        # print(type(result))
        print(sys.getsizeof(result_lsit))
        print(result_lsit[:10])
        return result_lsit
    
    def plot_somenumber(self):
        x = []
        for i in self.select_data():           
            print(i[1]/2491)
            x.append(i[1]/2491)
        print(x)
        print(sum(x)/16)
        
    
def main():
    t1 = time.time()
    use_getnumber()
    # analysis = AnalysisNumber()
    # analysis.select_data()
    print(time.time()-t1)
    
if __name__ == "__main__":
    main()
    