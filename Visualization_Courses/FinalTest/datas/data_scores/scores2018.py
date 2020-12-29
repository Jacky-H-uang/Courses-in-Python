# Created By Jacky on 2020/12/26

import requests
from bs4 import BeautifulSoup
import pandas
re = requests.get('https://zsb.whpu.edu.cn/info/1052/2055.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['省份', '批次','分数线']
list1 = []


for i in res:
    if not i.text.split()[2].isdigit():
        continue
    temp = list()
    # 单独处理湖北省
    if i.text.split()[1][:3].isdigit():
        temp.append('湖北')
        temp.append(i.text.split()[0])
        temp.append(i.text.split()[1][:3])
    else:
        temp.append(i.text.split()[0])
        temp.append(i.text.split()[1])
        temp.append(i.text.split()[2])
    list1.append(temp)

table = pandas.DataFrame(columns = all_, data = list1)
table.to_csv('2018年各省份录取分数线.csv')