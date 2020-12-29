# Created By Jacky on 2020/12/26

import requests
from bs4 import BeautifulSoup
import pandas
re = requests.get('https://zsb.whpu.edu.cn/info/1052/1831.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['省份', '批次','分数线']
list1 = []
for i in res:
    if not i.text.split()[3].isdigit():
        continue
    if i.text.split()[2] == '文史':
        continue
    temp = list()
    temp.append(i.text.split()[0])
    temp.append(i.text.split()[1])
    temp.append(i.text.split()[3])
    list1.append(temp)

table = pandas.DataFrame(columns = all_, data = list1)
table.to_csv('2017年各省份录取分数线.csv')