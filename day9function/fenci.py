import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image
with open('wenzhang.txt','r',encoding='utf-8')as file:
    text = file.read()
word = jieba.lcut(text)
print(word)
count = {}
image = Image.open('mask.jpg')#作为背景形状的图
graph = np.array(image)
for i in word:
    if len(i)>1:
        count[i]=count.get(i,0)+1
print(count)

wc = WordCloud(font_path='youyuan.ttf',
               width=1000,
               height=1000,
               max_words=600,
               background_color='white',
               mask = graph
               )


wc.generate_from_frequencies(count)
wc.to_file('cloud.jpg')

