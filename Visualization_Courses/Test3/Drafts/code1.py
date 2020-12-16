# Created By Jacky on 2020/11/21



from folium.plugins import HeatMap
import pandas as pd
import folium
import webbrowser
from folium import plugins
import json
import requests

# 每个街区的位置
map_location=[
    [-37.81522786515279, 144.96604718485247],
    [-37.818056369753606, 144.95668672649106],
    [-37.81822812913541, 144.95667521355585],
    [-37.81365793486913, 144.96449191114564],
    [-37.81389624831713, 144.96428649941234],
    [-37.81011741189866, 144.96272228230922],
    [-37.811530905351205, 144.9560422246367],
    [-37.80949561639754, 144.96524752806712],
    [-37.808862211033166, 144.9724556655564],
    [-37.81820214244847, 144.95249612888574],
    [-37.809454294081306, 144.94858671468288],
    [-37.813709072359586, 144.9427447925739],
    [-37.814116232884324, 144.93875379765464],
    [-37.82314011038058, 144.94731542649114],
    [-37.81790261876608, 144.97445122021648],
    [-37.819087925368514,144.96822828045552],
    [-37.81810478956018, 144.9670481084623],
    [-37.81987315184709, 144.96304426881844]
]
localName = pd.read_csv('2012_01-HOUR.CSV')
localName = localName.columns.tolist()[7:]


"""
Task : 
    数据集：墨尔本人行道监控数据
    任务：在地图上动态显示人流情况
"""




"""
            How to deal this task:
code1 : 解决 2009-05 ~ 2012-03 人口流动图
1. 先用 pandas 读取数据
2. 解析数据：
        将墨尔本所有的街区的每天的流动人口变化提出来
        然后形成形成映射
3. 可视化的形式是以热力图颜色分布来显示
    注意为动态显示，即每天热力图随着数据来变化
"""




# 加载数据, 加载一个文件
def loadData(file):
    data = pd.read_csv(file)
    n = len(data)
    y = []


    for i in range(n):
        x = []
        for j in range(7,25):
            temp = []
            temp.append(map_location[j-7][0])
            temp.append(map_location[j-7][1])
            if data.iloc[i,j] == '' or data.iloc[i,j] == ' ':temp.append(0)
            else : temp.append(float((int(data.iloc[i,j]) / 1000)))
            x.append(temp)
        y.append(x)
    return data , y




# Visualization
def plotter(filenames):
    m = folium.Map(
        location=[-37.81987315184709, 144.96304426881844],
        zoom_start = 12
    )

    sdata, data = loadData(filenames)

    Year = sdata.Year.tolist()
    Month = sdata.Month.tolist()
    Day = sdata.MDate.tolist()
    date = []
    for i , j , k in zip(Year,Month,Day):
        date.append([i,j,k])


    time_index = [x for x in range(0,len(date))]

    for i in range(len(map_location)):
        folium.Marker(
            [map_location[i][0] , map_location[i][1]] ,
            popup = localName[i],
            icon = folium.Icon(color='red', icon='info-sign'),
            tooltip = str(localName[i]),
        ).add_to(m)


    heatMap = plugins.HeatMapWithTime(
        data,
        auto_play = True,
        index = [
            str(x[0]) + "-"
            + str(x[1]) + "-"
            + str(x[2])
            + "  " + str(y%24) + " : 00"
            for x , y in zip(date,time_index)
        ],
        min_opacity = 0.6,
        name = "JACKYJACKYJACKY"
    ).add_to(m)

    m.save("code1.html")






# Test
if __name__ == '__main__':
    files = '2009_05-2012_03-HOUR.CSV'
    plotter(files)
