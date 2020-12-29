# Created By Jacky on 2020/12/27

"""
制作学院 2020 年招生的饼状图
"""

import pyecharts.options as opts
from pyecharts.charts import Pie
import pandas as pd

# 加载数据
def load_data():
    f = pd.read_csv('2020年学院招生.csv')
    x_data = f.学院.tolist()
    y_data = f._2020录取总数.tolist()

    return x_data , y_data

# 可视化
def plotter():
    x , y = load_data()
    data_pair = [list(z) for z in zip(x,y)]
    data_pair.sort(key = lambda x:x[1])
    (
        Pie()
        .add(
            series_name="招生比例",
            data_pair=data_pair,
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            # label_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
        .render("code5.html")
    )
if __name__ == '__main__':
    plotter()