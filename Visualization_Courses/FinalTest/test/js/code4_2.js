        var chart_57cf72772a7b4854b99638dd27076057 = echarts.init(
            document.getElementById('57cf72772a7b4854b99638dd27076057'), 'white', {renderer: 'canvas'});
        var option_57cf72772a7b4854b99638dd27076057 = {
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
            "name": "\u51b7\u95e8\u4e13\u4e1aTop10",
            "legendHoverLink": true,
            "data": [
                20,
                20,
                17,
                16,
                15,
                12,
                9,
                8,
                5,
                3
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
                "\u51b7\u95e8\u4e13\u4e1aTop10"
            ],
            "selected": {
                "\u51b7\u95e8\u4e13\u4e1aTop10": true
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
                "\u5916\u56fd\u8bed\u8a00\u6587\u5b66\u7c7b",
                "\u5de5\u5546\u7ba1\u7406\u7c7b",
                "\u5eb7\u590d\u6cbb\u7597\u5b66",
                "\u884c\u653f\u7ba1\u7406",
                "\u65c5\u6e38\u7ba1\u7406",
                "\u56fd\u9645\u7ecf\u6d4e\u4e0e\u8d38\u6613",
                "\u6587\u5316\u4ea7\u4e1a\u7ba1\u7406",
                "\u62a4\u7406\u5b66",
                "\u884c\u653f\u7ba1\u7406",
                "\u6587\u5316\u4ea7\u4e1a\u7ba1\u7406"
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
        chart_57cf72772a7b4854b99638dd27076057.setOption(option_57cf72772a7b4854b99638dd27076057);