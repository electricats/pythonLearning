import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image

def drawcloud(filename,imgname,maxword):
    with open(filename,'r',encoding='utf-8')as file:
        text = file.read()
    word = jieba.lcut(text)
    #print(word)
    count = {}
    image = Image.open(imgname)
    graph = np.array(image)

    for i in word:
        if len(i)>1:
            count[i]=count.get(i,0)+1
    print(count)

    stopword=['我们','不同','之间']
    for i in stopword:
        del count[i]

    wc = WordCloud(font_path='youyuan.ttf',
                   width=1000,
                   height=1000,
                   max_words=maxword,
                   background_color='white',
                   mask = graph
                   )


    wc.generate_from_frequencies(count)
    wc.to_file('cloud.jpg')



