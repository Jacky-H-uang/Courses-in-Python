# Created By Jacky on 2020/12/26

import requests
from bs4 import BeautifulSoup
import pandas
re = requests.get('https://xxgkw.whpu.edu.cn/info/1107/1999.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['省份', '录取数']
list1 = []
data_dic = dict()
for i in res:
    if i.text.split()[0] not in data_dic:
        data_dic[i.text.split()[0]] = int(i.text.split()[3])
    else :
        data_dic[i.text.split()[0]] += int(i.text.split()[3])

for i , j in data_dic.items():
    temp = list()
    temp.append(i)
    temp.append(str(j))
    list1.append(temp)


table = pandas.DataFrame(columns = all_, data = list1)
table.to_csv('2020年.csv')