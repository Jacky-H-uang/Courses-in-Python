 var chart_70bd9f511e8a42f7a95c93adab32c99b = echarts.init(
            document.getElementById('70bd9f511e8a42f7a95c93adab32c99b'), 'white', {renderer: 'canvas'});
        var option_70bd9f511e8a42f7a95c93adab32c99b = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u70ed\u95e8\u4e13\u4e1aTop10",
            "legendHoverLink": true,
            "data": [
                257,
                242,
                213,
                168,
                145,
                103,
                88,
                88,
                82,
                72
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u70ed\u95e8\u4e13\u4e1aTop10"
            ],
            "selected": {
                "\u70ed\u95e8\u4e13\u4e1aTop10": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "name": "\u4e13\u4e1a",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLabel": {
                "rotate": 30
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u98df\u54c1\u79d1\u5b66\u4e0e\u5de5\u7a0b\u7c7b",
                "\u673a\u68b0\u7c7b",
                "\u8ba1\u7b97\u673a\u7c7b",
                "\u571f\u6728\u7c7b",
                "\u7535\u5b50\u4fe1\u606f\u7c7b",
                "\u52a8\u7269\u79d1\u5b66",
                "\u5316\u5b66\u5de5\u7a0b\u4e0e\u5de5\u827a",
                "\u8bbe\u8ba1\u5b66\u7c7b",
                "\u81ea\u52a8\u5316",
                "\u73af\u5883\u5de5\u7a0b"
            ]
        }
    ],
    "yAxis": [
        {
            "name": "\u4e13\u4e1a\u5f55\u53d6\u6570",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLabel": {
                "rotate": 30,
                "color": "blue"
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_70bd9f511e8a42f7a95c93adab32c99b.setOption(option_70bd9f511e8a42f7a95c93adab32c99b);