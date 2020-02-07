# coding=utf-8
import random
# 每2740人中一个车牌
print("本测试纯属娱乐，无任何实用价值")
print("欢迎使用xx设计的车牌摇号模拟器，试试看你需要用多久才能摇到号吧！")
a = int(input("请输入一个1到2740之间的整数，按下回车"))
lucky = 0
time = 0
while lucky == 0:
    num = random.randint(1,2740)
    if num == a:
        print("恭喜你摇到号啦！")
        print("你一共花了"+str(time/6)+"年摇到了你的车牌！")
        lucky = 1
    else:
        time = time+1