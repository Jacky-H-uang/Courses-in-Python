import requests
from bs4 import BeautifulSoup
import pandas
re = requests.get('https://zsb.whpu.edu.cn/info/1052/2266.htm')
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'lxml')
res = res.find('tbody')
res = res.find_all('tr')[1:-1]
all_ = ['省份', '批次','分数线']
list1 = []
for i in res:
    if len(i.text.split()) < 10:
        continue
    temp = list()
    temp.append(i.text.split()[0][:2])
    temp.append(i.text.split()[1])
    if i.text.split()[9] == '-':
        temp.append(i.text.split()[10])
    else :
        temp.append(i.text.split()[9])
    list1.append(temp)


table = pandas.DataFrame(columns = all_, data = list1)
table.to_csv('2020年各省份录取分数线.csv')