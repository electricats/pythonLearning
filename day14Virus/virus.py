#coding='utf-8'
import requests
import json
from pyecharts import options as opts
from pyecharts.charts import *
from pyecharts.globals import ThemeType

def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'}
    res = requests.get(url, headers=headers).text
    c = json.loads(res)
    data = json.loads(c['data'])
    return data

def print_data_china():
    data = get_data()
    print('统计截至时间：'+str(data['lastUpdateTime']))
    print('全国确诊人数：'+str(data['chinaTotal']['confirm']))
    print('相较于昨天确诊人数：'+str(data['chinaAdd']['confirm']))
    print('全国疑似病例：'+str(data['chinaTotal']['suspect']))
    print('相较于昨天疑似人数：'+str(data['chinaAdd']['suspect']))
    print('全国治愈人数：'+str(data['chinaTotal']['heal']))
    print('相较于昨天治愈人数：'+str(data['chinaAdd']['heal']))
    print('全国死亡人数：'+str(data['chinaTotal']['dead']))
    print('相较于昨天死亡人数：'+str(data['chinaAdd']['dead']))

def print_data_path_china():
    data = get_data()['areaTree'][0]['children']
    mapdata=[]
    for char in data:
        mapdata.append([char['name'], char['total']['confirm']])
        char = char['children']
    area_map = Map()
    area_map.add("武汉加油", mapdata, "china", is_map_symbol_show=False)
    area_map.set_global_opts(title_opts=opts.TitleOpts(title="Map-疫情地图"),
                             visualmap_opts=opts.VisualMapOpts(max_=3000, is_piecewise=True,
                                                               pieces=[
                                                                   {"min": "0", "max": "10", "label": "0-10",
                                                                    "color": "#FFA07A"},
                                                                   {"min": "10", "max": "100", "label": "10-100",
                                                                    "color": "#FF7F50"},
                                                                   {"min": "100", "max": "1000", "label": "100-1000",
                                                                    "color": "#FF4500"},
                                                                   {"min": "1000", "max": "10000",
                                                                    "label": "1000-10000", "color": "#FF0000"},
                                                                   {"min": "10000", "max": "5000000", "label": ">10000",
                                                                    "color": "#B22222"},
                                                               ]))
    area_map.render("疫情地图.html")
    path_data = []
    path_china = []
    path = str(input('请输入你要查询的省份：'))
    for i in data:
        path_china.append(i['name'])
        path_data.append(i['children'])
    if path in path_china:
        num = path_china.index(path)
        data_path = path_data[num]
        for i in data_path:
            print(i['name']+" 地区今日疫情增长数："+str(i['today']['confirm']))
            print("总确诊数："+str(i['total']['confirm']))
            print("总疑似数：" + str(i['total']['suspect']))
            print("死亡率：" + str(i['total']['deadRate']))
            print("治愈数：" + str(i['total']['heal']))
            print("治愈率：" + str(i['total']['healRate']))
            print()

if __name__ == '__main__':
    get_data()
    print_data_china()
    while True:
        print_data_path_china()
