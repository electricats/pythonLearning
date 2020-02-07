# coding=utf-8
import random
# 每2740人 会有1个幸运儿诞生
print("本测试纯属娱乐，无任何实际参考价值")
a = input("请输入一个1到2740之间的数开始进行摇号时间评估")
lucky = 0   #是否中签
times = 0   #摇号期数

while lucky == 0:
    if(random.randint(1,2740) == int(a)):
        print("恭喜你中签啦！")
        print("中签的时间为：" + str(times/6)+ "年后")
        lucky =1
    else:
        times=times+1
