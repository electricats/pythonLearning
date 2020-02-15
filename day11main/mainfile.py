from day10 import ciyun
from Day7Hangman import *

userinput = input('请输入您要打开的应用程序 a.词云图 b.hangman小游戏')

if userinput=='a':
    print('欢迎使用词云生成软件，请输入您的词云文章（包含尾缀），图片蒙版（包含尾缀），以及词云字符数量')
    filename = input('请输入文字文件')
    img = input('请输入图片文件')
    num = int(input('请输入绘制的字符数量'))
    ciyun.drawcloud(filename, imgname=img, maxword=num)

elif userinput == 'b':
    print('欢迎进入hangman猜词小游戏')
    runhangman()