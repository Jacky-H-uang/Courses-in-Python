# Created By Jacky on 2020/12/26

import requests
from bs4 import BeautifulSoup
import pandas
re = requests.get('http://xxgkw.whpu.edu.cn/info/1119/2062.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['招生代码', '学院', '_2020录取总数']
list1 = []
for i in res:
    list1.append(i.text.split())
table = pandas.DataFrame(columns = all_, data = list1)
table.to_csv('2020年学院招生.csv')