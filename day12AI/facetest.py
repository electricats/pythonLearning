import json
import requests

url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
file = open('jay.jpg','rb')
img = {'image_file':file}

parameters = {
    'api_key':'Oj0rZ8uZ3QwTaN90XKRFIgRSRG1dplWR',
    'api_secret':'sPB6ZQXqxi5DCp1jhN9dDfk-ifJtsIfx',
    'return_attributes':'age,beauty,smiling,emotion',
}
receive = requests.post(url=url,files=img,data=parameters)
data = json.loads(receive.text)
#print(data['faces'][0]['attributes']['age']['value'])
#print(data['faces'][0]['attributes']['smile']['value'])
#print(data['faces'][0]['attributes']['emotion']['happiness'])

print("您的颜值在女性的角度得分为："+ str(data['faces'][0]['attributes']['beauty']['female_score']))


