# Created By Jacky on 2020/12/26


import requests
from bs4 import BeautifulSoup
import pandas
re = requests.get('https://xxgkw.whpu.edu.cn/info/1106/1752.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['省份', '录取数']
list1 = []
for i in res:
    temp = list()
    if not i.text.split()[1].isdigit():
        continue
    temp.append(i.text.split()[0])
    temp.append(i.text.split()[1])
    list1.append(temp)

print(list1)
table = pandas.DataFrame(columns = all_, data = list1)

table.to_csv('2019年.csv')