# coding=utf-8
import random
while True:
    user=input("1.石头 2.剪刀 3.布")
    computer = random.randint(1,3)
    if((user == 1 and computer == 2)or(user == 2 and computer == 3)or(user == 3 and computer == 1)):
        print("你赢了")
    elif user == computer:
        print("平局喔")
    else:
        print("你输了")