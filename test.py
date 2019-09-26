import os
import re
import sys
import json
import time
import lxml
import redis
import pprint
import random
import pymongo
import pymysql
import asyncio
import objgraph
import datetime
import requests
import threading
from lxml import etree
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from decimal import Decimal, ROUND_HALF_UP


def path():
    p = Path(".")
    for i in p.iterdir():
        print(i)
        # print(i.is_dir())


async def test_io():
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
    try:
        pass
    except Exception as e:
        print(e)

def paixu():
    """
    排序
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


def find_fun_num(l: list, n):
    """
    二分算法.....

    """
    if isinstance(l, list):
        if len(l) != 0:
            l.sort()
            # print(len(l))
            mid = Decimal(3)
            mid = mid.quantize(Decimal('0'), rounding=ROUND_HALF_UP)    # 消除逢5不进的情况。
            if l[mid] == n:
                return n
            
        else:
            print("列表长度为0：")
    else:
        print("l 不是列表")
    

def fib(n):
    """
    数列
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)


def find_num_one(l: list):
    """
    查找列表中的数字.....
    """
    if isinstance(l, list):
        for i in l:
            # print(i)
            if len(str(i)) == 1:
                print(i)
    else:
        print("l is not list type")


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
    快速排序
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


def binary_computer(l: int):
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
    

def write_in_redis(key_name: str, value: list):
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    for l in value:
        r.sadd(key_name, l)


def operating_mysql():
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

    pass

def time_test():
    n = 0
    num = 0
    while n < 100000:
        num += n
        n += 1
        # print(num)
    print(num)


def mutil_process():
    print('This is test...')
    
    time.sleep(1)
    

def main():
    t1 = time.time()
    l = [1, 2, 12, 14, 54, 9, 0, 10, 12, 11]
    s = '+-+++-+++---+-+-++++--'

    t2 = time.time() - t1
    print(t2)


if __name__ == '__main__':
    main()
