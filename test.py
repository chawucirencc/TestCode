import os
import re
import sys
import json
import time
import lxml
import redis
import jieba
import pkuseg
import pprint
import random
import pymongo
import pymysql
import asyncio
import objgraph
import datetime
import requests
import threading
import matplotlib.pyplot as plt
from lxml import etree
from pyquery import PyQuery as pq
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import Counter
from fake_useragent import UserAgent
from decimal import Decimal, ROUND_HALF_UP
from selenium.webdriver.common.keys import Keys


def path():
    p = Path(".")
    for i in p.iterdir():
        print(i)
        # print(i.is_dir())


async def test_io():
    """
    异步...
    """
    t1 = time.time()
    print("1")
    # await asyncio.sleep(1)
    print("2")
    t2 = time.time() - t1
    print(t2)


def san():
    """
    三元算法.....
    """
    a, b = 1, 2
    c = a + b if a > b else a - b
    print(c)


def get_page_xpath():
    """
    获取网页响应......
    使用 Xpath 获取结果
    """
    try:
        url = 'https://www.baidu.com/'
        response = requests.get(url)
        assert response.status_code == 200
        # print(response.status_code)
        response.encoding = 'utf-8'
        res = etree.HTML(response.text)
        res_tree = res.xpath(".//a[@class='mnav']//text()")
        print(res_tree)
    except Exception as e:
        print(e)


def get_page_beautiful():
    """
    使用 CSS 选择器提取数据。
    """
    try:
        url = 'https://www.baidu.com/'
        response = requests.get(url)
        assert response.status_code == 200
        # print(response.status_code)
        response.encoding = 'utf-8'
        res = BeautifulSoup(response.text, 'lxml')
        # print(res.prettify())
        # result = res.findAll('a', attrs ={'class':'mnav'})
        # result = res.select('.mnav')
        result = res.select('a[class=mnav]')
        print(list_to_text(result))
    except Exception as e:
        print(e)


def list_to_text(result: list):
    """
    列表生成器...
    """
    a = [x.text for x in result]
    return a


def test_ua_ip(url_1):
    """
    IP测试.....
    """
    url = "http://httpbin.org/get"
    url_1 = ' http://45.78.69.34:8090/min/'
    res = requests.get(url_1)
    page_tree = etree.HTML(res.text)
    info = page_tree.xpath("//body//text()")[0]
    print(type(info))

    ip_pool = ['120.78.225.5:3128', '14.115.107.17:808', '218.66.253.144:8800',
    '27.46.23.218:8888']
    for i in range(50):
        print(i)
        ran = random.choice(ip_pool)
        headers = {
        # "User-Agent": ua.random
        }
        proxies = {
        'http': 'http://'+ ran,
        'https': 'https://' + ran
        }
        res = requests.get(url_1, headers=headers, proxies=proxies)
        print(res.status_code)
        print(res.text)
        print(ran)
        print(proxies)
    return 0


def get_day(n):
    """
    获取天数......
    """
    if type(n) is int:
        now_time = datetime.datetime.now()
        print("今天是{0}".format(str(now_time).replace('-', '')[:9]))
        d = now_time + datetime.timedelta(n)
        if n > 0:
            print("{0}天后的日期是:{1}".format(n, str(d).replace(r'-', '')[:9]))
        elif n == 0:
            print("就是今天哦！")
        else:
            print("{0}天前的日期是:{1}".format(n*-1, str(d).replace(r'-', '')[:9]))
    else:
        print("输入的不是整数.")


def f1(n):
    def f2(*args):
        s = 10
        return s * n
    return f2


def strappend(num):
    str='first'
    for i in range(num):
        # str+=str(i)
        print(i)
    return str


def get_page_info(url):
    """
    此函数可以创建一个 requests 会话用来获取 POST 请求的 cookies。
    通过 session 会话可以将 cookies传递到下次的 get 请求当中。                 
    """
    session = requests.Session()
    param = {'username': 'username', 'password': 'password'}
    r_post = session.post(url, param=param)
    print(r_post.cookies)
    r_get = session.get(url)
    print(r_get.text)


class Foo(object):
    """
    猴子补丁
    """
    def fun1(self):
        print('This is fun1')


def fun2(**args):
    print('Thsi is fun2')


def fun3(**args):
    print('This is fun3')


def fun4(*args, **kwargs):
    print(*args)
    # print(type(args))
    print(**kwargs)
    # print(type(kwargs))


def err():
    """
    测试网页响应错误....
    """
    url = "https://www.baidu.com/"
    res = requests.get(url)
    try:
        res.status_code == 200
        res.encoding = "utf-8"
        print(res.text)
        return res.text
    except Exception as er:
        print("get page_info error")
        print(er)

sys.setrecursionlimit(2000)
def recursion(n):
    """
    测试默认递归次数.....
    """
    print(n) 
    recursion(n + 1) 


class Cl1:
    def cl1_fun1(self):
        print("This is cl1_fun1")
    
    def cl1_fun2(self):
        print("This is cl1_fun2")


class Cl2(Cl1):
    def cl1_fun1(self):
        super().cl1_fun1()
        print("This is cl2_fun1")
        
    def cl2_fun2(self):
        print("This is cl2_fun2")


def catch_error():
    """
    错误捕获...
    """
    try:
        pass
    except Exception as e:
        print(e)

def paixu():
    """
    排序.....
    关于sorted()和a.sort()的用法...
    """
    a = [1, 8, 3, 5, 3, 0, 6, 9]
    # a.sort()
    # print(a)
    # print(sorted(a))
    # print(a)
    pprint.PrettyPrinter(indent=1, width=8)
    pprint.pprint(a)


def time_complex():
    """
    时间复杂度.....
    """
    t1 = time.time()
    a = [1, 2, 3, 4]
    b = {1, 2, 3, 4}
    # a.append(5)
    b.add(5)
    print(b)
    t2 = time.time() - t1
    print(t2)


def find_fun_num(l: list, b: int, e: int, f: int):
    """
    二分查找算法.....
    b 为列表第一个元素索引位置。
    e 为列表元素最后一个索引的位置。
    n 为要查找的元素

    """
    if isinstance(l, list):
        if len(l) != 0:
            l.sort()
            # print(len(l))
            # print(l)
            mid = Decimal((b+e)/2)
            mid = mid.quantize(Decimal('0'), rounding=ROUND_HALF_UP)    # 消除逢5不进的情况。
            if l[int(mid)] == f:
                print(f)
                print(l.index(f))
                print(mid)
            elif mid < f:
                print(find_fun_num(l, mid, e, f))
            else:
                print(find_fun_num(l, b, mid, f))
                
            
                
            
        else:
            print("列表长度为0：")
    else:
        print("l 不是列表")
    

def fib(n):
    """
    斐波那契数列...
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)


def find_num_one(l: list):
    """
    查找列表中的单个位数的数字.....
    """
    if isinstance(l, list):
        for i in l:
            # print(i)
            if len(str(i)) == 1:
                print(i)
    else:
        print("l is not list type")


def find_same_number_function1(l: list):
    """
    方法1：
    查找列表中的重复数字...
    这种方法返回的结果是一个<class 'collections.Counter'>，
    """
    if isinstance(l, list):
        res = Counter(l)
        # print(res.most_common())
        # print(res[12])

    else:
        print("l is not lsit type...")
    pass


def find_same_number_function2(l: list):
    """
    方法2：
    这种方法直接返回的是一个字典，可以更方便的处理...
    """
    same_number = {}
    if isinstance(l, list):
        for i in l:
            same_number[i] = l.count(i)

    else:
        print("l不是列表")
    

def find_same_number_function3(l:list):
    """
    方法3：
    这种方法只能找出重复元素，还不能返回重复次数。可以结合第一个和第二个函数一起使用...
    """
    new_ls = []
    same_list = []
    same_number = {}
    if isinstance(l, list):
        for i in l:
            if i not in new_ls:
                new_ls.append(i)
            else:
                same_list.append(i)
    else:
        print("l不是列表")
    print('重复的有：', same_list)
    

def bubble_sort(l: list):
    """
    冒泡排序.....
    """
    if isinstance(l, list):
        for i in range(len(l)-1):
            for j in range(len(l) - 1):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j+1], l[j]
    else:
        print("l is not list type")
    print(l)     


def fast_sort(l: list):
    """
    快速排序......
    """
    if isinstance(l, list):
        pass
    else:
        print("l is not list type")
    pass


def topology_sort(l: list):
    """
    拓扑排序
    """
    if isinstance(l, list):
        pass
    else:
        print("l is not list type")


def binary_computer(a: int, b: int):
    """
    二进制计算
    """

    pass


def change_add(s: str):
    """
    改变 + - 的位置。
    """
    ad = ''
    le = ''
    for i in s:
        if i == '+':
            ad += i
        else:
            le += i
    result = ad + le
    print(result)
    

def creatr_thing():
    """
    mysql查询...
    """
    try:
        db = pymysql.connect(host='localhost', user='root', password='password', database='world')
        db.autocommit(True)
        db_curs = db.cursor()
        print('连接成功...')
        sql_ = "select * from city\
                where CountryCode='NLD'"
        db_curs.execute(sql_)
        result = db_curs.fetchall()
        print(type(result))
        for i in result:
            print(i)
    except Exception as err:
        print(err)
    

def operating_redis():
    """
    操作redis...
    """
    try:
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        # print("连接成功...")
        movie_date = r.lrange('movie_date', 0, -1)
        movie_name = r.lrange('movie_name', 0, -1)
        movie_url = r.lrange('movie_url', 0, -1)
        
        movie_date_new = list(set(movie_date))
        movie_name_new = list(set(movie_name))
        movie_url_new = list(set(movie_url))

        write_in_redis('movie_date_new', movie_date_new)
        write_in_redis('movie_name_new', movie_name_new)
        write_in_redis('movie_url_new', movie_url_new)
    except Exception as err:
        print(err)
    

def write_in_redis(key_name: str, value: list):
    """
    写入数据到redis(辅助函数)
    """
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    for l in value:
        r.sadd(key_name, l)     # 往集合中添加数据


def operating_mysql():
    """
    操作mysql...
    """
    try:
        db = pymysql.connect(host='localhost', user='root', password='password', database='world')
        db.autocommit(True)
        db_curs = db.cursor()
        print('连接成功...')
        select_sql = 'select movie_name FROM dytt_1'
        db_curs.execute(select_sql)
        result = db_curs.fetchall()
        print('set:', len(set(result)))
        print('tuple:', len(result))
    except Exception as err:
        print(err)


def operating_mongodb():
    """
    操作mongodb...
    """
    try:
        myclinent = pymongo.MongoClient('localhost', 27017)
        mydb = myclinent.dytt_movie	# 连接到数据库
        result_data = mydb.test	# 连接到数据库中的集合
        # for i in result_data.find(): 
        #     print(i)	# 查找集合中的每个数据，并输出。
        result_one = result_data.find_one({'id': 1})
        print(result_one)
        print(type(result_one))  #查看单条结果的数据类型。
    except Exception as err:
        print(err)
    

def time_test():
    """
    输出时间测试...
    """
    n = 0
    num = 0
    while n < 100000:
        num += n
        n += 1
        # print(num)
    print(num)


def mutil_process_1():
    """
    多线程1...
    """
    for _ in range(1000):
        print('This is test_1...')


def mutil_process_2():
    """
    多线程2...
    """
    for _ in range(1000):
        print('This is test_2')
    

def mutil_process():
    """
    多线程测试
    """
    mutil_process_1()
    mutil_process_2()
    # t1 = threading.Thread(target=mutil_process_1, name='mutil_process_thread_1')
    # t2 = threading.Thread(target=mutil_process_2, name='mutil_process_thread_2')
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()


def sele():
    """
    selenium测试
    """
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    # driver.close()
    time.sleep(5)
    # driver.refresh()
    # element = driver.find_element_by_link_text("新闻")
    driver.find_element_by_id("kw").send_keys("seleniumm")
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("kw").send_keys(Keys.SPACE)
    driver.find_element_by_id("kw").send_keys("教程")
    driver.find_element_by_id("su").send_keys(Keys.ENTER)
    driver.find_element_by_id()
    driver.quit()
    
    
class WordFrequency():
    def page_info(self, url):
        try:
            pass
        except Exception as err:
            print("error", err)
            
        pass
    def main(self):
        url = " "
        pass

class Hash:
    """
    简单Hash表
    """
    def __init__(self):
        self.capacity = 11
        self.hash_table = [[None, None] for i in range(self.capacity)]
        self.num = 0
        self.load_factor = 0.75
        
    def hash(self, k, i):
        # Hash函数（映射函数）。
        h_value = (k+i) % self.capacity
        if self.hash_table[h_value][0]==k:
            return h_value
        if self.hash_table[h_value][0]!=None:
            i+=1
            h_value=self.hash(k, i)
        return h_value
    
    def resize(self):
        self.capacity = self.num*2
        temp = self.hash_table[:]
        self.hash_table = [[None, None] for i in range(self.capacity)]
        for i in temp:
            # 把原来的元素存入。
            if (i[0]!=None):
                hash_v = self.hash(i[0], 0)
                self.hash_table[hash_v][0] = i[0]
                self.hash_table[hash_v][1] = i[1]
    
    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v
        
        self.num += 1
        if (self.num/len(self.hash_table))>self.load_factor:
            self.resize()
    
    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]
                  

def binarySearch(arr,beg,end,item):  
    """
    二分查找算法。（网上版本）参考，对于无序数组或者列表支持不佳。
    """
    arr.sort()
    if end >= beg:  
        mid = int((beg+end)/2)  
        if arr[mid] == item :  
            return mid+1  
        elif arr[mid] < item :   
            return binarySearch(arr,mid+1,end,item)  
        else:   
            return binarySearch(arr,beg,mid-1,item)  
    return -1  


def find_er_num():
    item = int(input("Enter the item which you want to search ?"))  
    arr=[16, 19, 20, 23, 45, 56, 78, 90, 96, 100];  
    l = [1, 2, 12, 14, 54, 9, 0, 10, 12, 11]
    location = -1;   
    location = binarySearch(l,0,8,item);  
    if location != -1:   
        print("Item found at location %d" %(location))  
    else:   
        print("Item not found")


class GetIPinfo:
    """
    IP测试类，
    """
    def __init__(self, url):
        self.url = url
        
    def getstatus(self):
        try:
            res = requests.get(self.url)
            res.status_code == 200
            res.encoding = "utf-8"
            # print(res.text)
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
    """
    使用pyquery请求解析网页！
    """
    def __init__(self, url):
        self.url = url
    
    def sendRequest(self):
        response = pq(self.url)
        print(type(response))
        print(response)
        
    def parseHtml(self):
        pass 


def use_pkuseg():
    # seg=pkuseg.pkuseg()
    # text=seg.cut('中华人民共和国今天成立了！')
    text=jieba.cut('中华人民共和国今天成立了！')
    print('、'.join(text))

def main():
    t1 = time.time()
    # l = [1, 2, 12, 14, 54, 9, 0, 10, 12, 11]
    # s = '+-+++-+++---+-+-++++--'
    # find_er_num()
    use_pkuseg()
    t2 = time.time() - t1
    print(t2)


if __name__ == '__main__':
    main()
