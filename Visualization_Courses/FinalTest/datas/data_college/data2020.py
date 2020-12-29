# Created By Jacky on 2020/12/27

import requests
from bs4 import BeautifulSoup
import pandas

re = requests.get('https://zsb.whpu.edu.cn/xxcx/zsjhcx/y2020n/hbs.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['专业名称', '录取数']
list1 = []
for i in res:
    temp = list()
    temp.append(i.text.split()[0])
    temp.append(i.text.split()[3])
    list1.append(temp)


table = pandas.DataFrame(columns = all_, data = list1)
table.to_csv('2020年湖北省各专业录取数量.csv')