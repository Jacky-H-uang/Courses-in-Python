# Created By Jacky on 2020/12/8



"""
This is a simple program to help classmate understand the test3 : )
"""
from folium.plugins import HeatMap
import pandas as pd
import folium
from folium import plugins


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

name1 = pd.read_csv('2012_01-HOUR.CSV')
name2 = name1.columns.tolist()[7:]




if __name__ == '__main__':

    data = pd.read_csv('2012_01-HOUR.CSV')
    n = len(data)
    x2 = []


    for i in range(n):
        x1 = []
        for j in range(7,25):
            t = []
            t.append(map_location[j-7][0])
            t.append(map_location[j-7][1])
            t.append(float((data.iloc[i,j]/100)))
            x1.append(t)
        x2.append(x1)

    m = folium.Map([-37.81987315184709, 144.96304426881844],zoom_start=10)

    d = x2

    # »»¡¶Õº
    heatMap = plugins.HeatMapWithTime(
        d,
        auto_play = True,
        min_opacity = 0.6,
    ).add_to(m)

    m.save("solution.html")