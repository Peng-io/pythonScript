import copy

beijing = {"GDP": 35371.28, "总人口": 1375.8, "平均房价": 37420.19, "平均工资": 145766, "地铁总里程": 699.3,
           "高校总数": 116, "三甲医院": 78, "小学生数量": 91.3}
shanghai = {"GDP": 35155.32, "总人口": 1462.38, "平均房价": 28981.11, "平均工资": 140400, "地铁总里程": 705,
            "高校总数": 78, "三甲医院": 66, "小学生数量": 80.02}
shenzhen = {"GDP": 26927.09, "总人口": 454.70, "平均房价": 55441.01, "平均工资": 111709, "地铁总里程": 303.4,
            "高校总数": 8, "三甲医院": 66, "小学生数量": 102.8}
guangzhou = {"GDP": 23628.60, "总人口": 927.69, "平均房价": 21581.27, "平均工资": 111839, "地铁总里程": 513,
             "高校总数": 91, "三甲医院": 62, "小学生数量": 105.85}
chengdu = {"GDP": 17012.65, "总人口": 1476.05, "平均房价": 9783.16, "平均工资": 88011, "地铁总里程": 302.285,
           "高校总数": 68, "三甲医院": 29, "小学生数量": 94.2}
chongqing = {"GDP": 23605.77, "总人口": 1962.66, "平均房价": 8189.98, "平均工资": 78928, "地铁总里程": 313.36,
             "高校总数": 69, "三甲医院": 27, "小学生数量": 126.15}
hangzhou = {"GDP": 15373, "总人口": 774.10, "平均房价": 24360.20, "平均工资": 106709, "地铁总里程": 135.36,
            "高校总数": 46, "三甲医院": 20, "小学生数量": 59.1}
wuhan = {"GDP": 17157, "总人口": 883.73, "平均房价": 12678.48, "平均工资": 88327, "地铁总里程": 339, "高校总数": 90,
         "三甲医院": 36, "小学生数量": 57.9}
xiAn = {"GDP": 9321.19, "总人口": 986.87, "平均房价": 9984.54, "平均工资": 87125, "地铁总里程": 155.66, "高校总数": 75,
        "三甲医院": 41, "小学生数量": 73.09}
tianjin = {"GDP": 14104.28, "总人口": 1081.63, "平均房价": 15924.26, "平均工资": 100731, "地铁总里程": 233,
           "高校总数": 71, "三甲医院": 49, "小学生数量": 67.32}
list_1 = {"北京": beijing, "上海": shanghai, "深圳": shenzhen, "广州": guangzhou, "成都": chengdu, "重庆": chongqing,
          "杭州": hangzhou, "武汉": wuhan, "西安": xiAn, "天津": tianjin}
info = {}
aggregate = {}
Sum = {}
for i in list_1:  # 北京
    for j in list_1[i]:  # GDP
        for l in list_1:
            info[l] = list_1[l][j]
        aggregate[j] = copy.deepcopy(info)


def my_sort(aggregate):
    for i in aggregate.values():
        No = 10
        j = sorted(i.items(), key=lambda x: x[1], reverse=True)
        for k in j:
            Sum[k[0]] = No
            No = No - 1
    return Sum


if __name__ == '__main__':
    print(my_sort(aggregate))
