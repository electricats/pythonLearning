import requests
import json

def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {'user-agent':'User-Agent: Mozilla/5.0 (Linux; X11)'}
    result = requests.get(url, headers = headers).text
    result1 = json.loads(result)
    finalresult = json.loads(result1['data'])
    return(finalresult)
    #print("确诊人数为："+ str(finalresult['chinaTotal']['confirm']))

def print_data(list):
    print('统计截至时间：'+str(list['lastUpdateTime']))
    print('全国确诊人数：'+str(list['chinaTotal']['confirm']))
    print('相较于昨天确诊人数：'+str(list['chinaAdd']['confirm']))
    print('全国疑似病例：'+str(list['chinaTotal']['suspect']))
    print('相较于昨天疑似人数：'+str(list['chinaAdd']['suspect']))
    print('全国治愈人数：'+str(list['chinaTotal']['heal']))
    print('相较于昨天治愈人数：'+str(list['chinaAdd']['heal']))
    print('全国死亡人数：'+str(list['chinaTotal']['dead']))
    print('相较于昨天死亡人数：'+str(list['chinaAdd']['dead']))


finallist = get_data()
print_data(finallist)
print(finallist['areaTree'][0]['children'])