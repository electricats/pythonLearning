import requests
from bs4 import BeautifulSoup
import os

for page in range(1, 2000):
    url = 'https://fabiaoqing.com/biaoqing/lists/page/'+str(page)+'.html'
    print("now at page:"+ url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    img_list = soup.find_all('img', class_='ui image lazy')

    for img in img_list:
        image = img.get('data-original')
        title = img.get('title')
        # print(image)
        with open(title + os.path.splitext(image)[-1], 'wb') as f:
            img = requests.get(image).content
            f.write(img)
