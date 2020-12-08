# Created By Jacky on 2020/12/5


"""

This file is just a draft and it's useful.

"""


import pandas as pd
import folium
import webbrowser
from folium import plugins
import json
import requests



latitude = 37.77
longitude = -122.42




cdata = pd.read_csv('test.csv')

data = cdata.iloc[0:200,:]



# # 循环添加热力图
# incidents = folium.map.FeatureGroup()
# for lat , lng in zip(cdata.Y,data.X):
#     incidents.add_child(
#         folium.CircleMarker(
#             [lat,lng],
#             radius = 7,
#             color = 'yellow',
#             fill = True,
#             fill_color = 'red',
#             fill_opacity = 0.4
#         )
#     )
#
#
#
# # 将热力图添加到地图当中
# san_map = folium.Map(location=[latitude,longitude],zoom_start=12)
# san_map.add_child(incidents)
#
#
#
# # 添加地理标签
# latitudes = list(data.Y)
# longitudes = list(data.X)
# labels = list(data.Category)
# for lat , lng , lab in zip(latitudes,longitudes,labels):
#     folium.Marker([lat,lng] , popup=lab).add_to(san_map)
#
#
#
# # Clean all the datas
# san_map = folium.Map(location = [latitude,longitude] , zoom_start = 12)
#
#
# # 统计区域犯罪总数
# incidents = plugins.MarkerCluster().add_to(san_map)
#
# for lat , lng , lab in zip(latitudes,longitudes,labels):
#     folium.Marker(
#         location = [lat,lng],
#         icon = None,
#         popup = lab
#     ).add_to(incidents)
#
# san_map.add_child(incidents)
#
#
#
#
#
# # 读取geojson文件，可视化旧金山市10个不同Neighborhood的边界
# url = 'https://cocl.us/sanfran_geojson'
# san_geo = f'{url}'
# san_map = folium.Map(location=[37.77, -122.4], zoom_start=12)
#
# folium.GeoJson(
#     san_geo,
#     style_function = lambda feature: {
#         'fillColor' : '#ffff00',
#         'color' : 'black',
#         'weight' : 2,
#         'dashArray' : '5,5'
#     }
# ).add_to(san_map)
#
#
#
# # 统计每个区域的犯罪事件数目
# disdata = pd.DataFrame(cdata['PdDistrict'].value_counts())
# disdata.reset_index(inplace = True)
# disdata.rename(columns = {'index' : 'Neighborhood' , 'PdDistrict' : 'Count'} , inplace = True)
# print(disdata)
#
#
#
# # 创建Choropleth Map （颜色深浅代表各区犯罪事件数目）
# san_map = folium.Map(location=[37.77, -122.4], zoom_start=12)
# folium.Choropleth(
#     geo_data=san_geo,
#     data=disdata,
#     columns=['Neighborhood','Count'],
#     key_on='feature.properties.DISTRICT',
#     #fill_color='red',
#     fill_color='YlOrRd',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     highlight=True,
#     legend_name='Crime Counts in San Francisco'
# ).add_to(san_map)



# # 创建热力图
# from folium.plugins import HeatMap
#
# san_map = folium.Map(location = [latitude, longitude], zoom_start = 12)
#
# heatdata = data[['Y','X']].values.tolist()
#
# print(heatdata)
#
#
# HeatMap(heatdata).add_to(san_map)







outfile = 'test.html'
san_map.save(outfile)
webbrowser.open(outfile,new = 2)