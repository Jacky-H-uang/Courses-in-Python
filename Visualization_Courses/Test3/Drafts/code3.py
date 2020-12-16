# Created By Jacky on 2020/12/12


"""
code 3: 将所有的 csv 文件合并到一起 其中去除重叠的部分
"""

from folium.plugins import HeatMap
import pandas as pd
import folium
import webbrowser
from folium import plugins
import re
import requests
import os


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
加载数据
"""
def loadData(filename):
    data = pd.read_csv(filename)

    return data




"""
解析数据：
    将多个 csv 文件整合成一个list
"""
def parserData(filenames):
    ret = []
    dataSet = []
    for f in filenames:
        data = loadData(f)
        n = len(data)
        dataSet.append(data)

        for i in range(n):
            subdata = []
            for j in range(7,25):
                temp = []
                temp.append(map_location[j-7][0])
                temp.append(map_location[j-7][1])

                # 清洗数据
                if data.iloc[i,j] == '' or data.iloc[i,j] == ' ': temp.append(0)
                # 除以 1000 避免权重过大而显示不出来
                else : temp.append(float(data.iloc[i,j])/1000)

                subdata.append(temp)
            ret.append(subdata)

    return dataSet , ret




"""
Visualization
"""
def plotter(filenames):
    m = folium.Map(
        location = [-37.81987315184709, 144.96304426881844],
        zoom_start = 12
    )

    dataSet , data = parserData(filenames)

    Time = []
    # 解决时间条的索引问题
    for d in dataSet:
        Year = d.Year.tolist()
        Month = d.Month.tolist()
        Mdate = d.Mdate.tolist()

        for i , j , k in zip(Year,Month,Mdate):
            Time.append([i,j,k])


    time_index = [x for x in range(0,len(data))]

    heatMap = plugins.HeatMapWithTime(
        data,
        auto_play = True,
        index = [
            str(x[0]) + "-"
            + str(x[1]) + "-"
            + str(x[2])
            + "  " + str(y%24) + " : 00"
            for x , y in zip(Time,time_index)
        ],
        min_opacity = 0.6
    ).add_to(m)

    # 一些附加的功能
    addMarker(m)        # 添加标记

    m.save("code3.html")




"""
添加功能：
    向热力图中添加点标记和地点的名字
"""
def addMarker(map):
    icon = ""
    path = 'https://raw.githubusercontent.com/Jacky-H-uang/Courses-in-Python/master/Visualization_Courses/Test3/Images/{}'.format
    for i in range(len(map_location)):
        # 对每个地点的图标来标记
        if re.search('Bridge',localName[i]):
            icon = path('bridge.png')
        elif re.search('City',localName[i]):
            icon = path('city.png')
        elif re.search('Station',localName[i]):
            icon = path('station.png')
        elif re.search('Library',localName[i]):
            icon = path('library.png')
        elif re.search('Street',localName[i]):
            icon = path('streetsign.png')
        else:
            icon = path('others.png')

        icon = folium.CustomIcon(
            icon
        )
        folium.Marker(
            [map_location[i][0] , map_location[i][1]] ,     # 经纬度
            popup = localName[i],                           # 地点名字
            icon = icon,
            tooltip = str(localName[i]),
        ).add_to(map)









# Test
if __name__ == '__main__':
    filenames = [
        '2009_05-2012_03-HOUR.CSV',
        '2012_04-HOUR.CSV',
        '2012_05-HOUR.CSV',
        '2012_06-HOUR.CSV',
        '2012_07-HOUR.CSV',
        '2012_08-HOUR.CSV',
        '2012_09-HOUR.CSV'
    ]

    plotter(filenames)