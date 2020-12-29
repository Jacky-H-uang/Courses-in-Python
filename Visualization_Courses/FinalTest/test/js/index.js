window.onload = function() {
	/* 地图 */
	var map = new BMap.Map("allmap"); // 创建Map实例
	map.centerAndZoom(new BMap.Point(114.228926, 30.659446), 18); // 初始化地图,设置中心点坐标和地图级别
	/* 信息窗口 */
	map.setCurrentCity("金银湖校区"); // 设置地图显示的城市 此项是必须设置的
	map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
	/* 地图控件和标注 */
	var point = new BMap.Point(114.228695, 30.658792);
	var marker1 = new BMap.Marker(point); // 创建标注
	map.addOverlay(marker1); // 将标注添加到地图中
	var opts1 = {
		width: 200, // 信息窗口宽度
		height: 100, // 信息窗口高度
		title: "武汉轻工大学图书馆", // 信息窗口标题
		message: "图书馆"
	}
	var infoWindow1 = new BMap.InfoWindow(
		"1980年起独立建馆,2009年金银湖校区图书馆建成启用,内含丰富藏书。", opts1); // 创建信息窗口对象
	marker1.addEventListener("click", function() {
		map.openInfoWindow(infoWindow1, point1); //开启信息窗口
	});

	var point2 = new BMap.Point(114.231102, 30.657008);
	var marker2 = new BMap.Marker(point2); // 创建标注
	map.addOverlay(marker2); // 将标注添加到地图中
	var opts2 = {
		width: 200, // 信息窗口宽度
		height: 100, // 信息窗口高度
		title: "数学与计算机学院", // 信息窗口标题
		message: "数学与计算机学院"
	}
	var infoWindow2 = new BMap.InfoWindow(
		" 现有计算机科学与技术、软件工程、网络工程、数字件工程”,目前在校本科生、研究生1600余名。",
		opts2); // 创建信息窗口对象
	marker2.addEventListener("click", function() {
		map.openInfoWindow(infoWindow2, point2); //开启信息窗口
	});

	var point3 = new BMap.Point(114.229292, 30.661812);
	var marker3 = new BMap.Marker(point3); // 创建标注
	map.addOverlay(marker3); // 将标注添加到地图中
	var opts3 = {
		width: 200, // 信息窗口宽度
		height: 100, // 信息窗口高度
		title: "机械工程学院", // 信息窗口标题
		message: "机械工程学院"
	}
	var infoWindow3 = new BMap.InfoWindow(
		"武汉轻工大学机械工程学院成立于1983年，1986年招收首届食品机械专业本科生，2004年开始招收研究生。",
		opts3); // 创建信息窗口对象
	marker3.addEventListener("click", function() {
		map.openInfoWindow(infoWindow3, point3); //开启信息窗口
	});

	var point4 = new BMap.Point(114.229952, 30.658989);
	var marker4 = new BMap.Marker(point4); // 创建标注
	map.addOverlay(marker4); // 将标注添加到地图中
	var opts4 = {
		width: 200, // 信息窗口宽度
		height: 100, // 信息窗口高度
		title: "艺术与传媒学院", // 信息窗口标题
		message: "艺术与传媒学院"
	}
	var infoWindow4 = new BMap.InfoWindow(
		"艺术与传媒学院,潮流与文化并存。",
		opts4); // 创建信息窗口对象
	marker4.addEventListener("click", function() {
		map.openInfoWindow(infoWindow4, point4); //开启信息窗口
	});


	var point5 = new BMap.Point(114.227154, 30.656989);
	var marker5 = new BMap.Marker(point5); // 创建标注
	map.addOverlay(marker5); // 将标注添加到地图中
	var opts5 = {
		width: 200, // 信息窗口宽度
		height: 100, // 信息窗口高度
		title: "经济与管理学院", // 信息窗口标题
		message: "经济与管理学院"
	}
	var infoWindow5 = new BMap.InfoWindow(
		"经济与管理学院建于1984年,现有老师和学生2600余名。", opts5); // 创建信息窗口对象
	marker5.addEventListener("click", function() {
		map.openInfoWindow(infoWindow5, point5); //开启信息窗口
	});

	var point6 = new BMap.Point(114.228699, 30.659849);
	var marker6 = new BMap.Marker(point6); // 创建标注
	map.addOverlay(marker6); // 将标注添加到地图中
	var opts6 = {
		width: 200, // 信息窗口宽度
		height: 100, // 信息窗口高度
		title: "金银湖校区", // 信息窗口标题
		message: "金银湖校区"
	}
	var infoWindow6 = new BMap.InfoWindow(
		"武汉轻工大学金银湖校区", opts6); // 创建信息窗口对象
	marker6.addEventListener("click", function() {
		map.openInfoWindow(infoWindow6, point6); //开启信息窗口
	});

	// 使用刚指定的配置项和数据显示图表。
	myChart.setOption(option);
}