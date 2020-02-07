# coding=utf-8
score = 0
print("来参加这个小测试，试验一下你有多了解我吧！")
print("题目1：我喜欢什么颜色？")
print("a：黑色black？")
print("b：白色white？")
print("c：粉红色pink？")
ans = input("please input your answer ")
if ans == "a":
    print("恭喜你选对啦！")
    score = score +10
else:
    print("你猜错啦！")

print("题目2：我喜欢吃什么？")
print("a：蔬菜vegetables？")
print("b：汉堡burgers？")
print("c：鱼fish？")
ans = input("please input your answer ")
if (ans == "b"):
    print("恭喜你选对啦！")
    score = score +10
else:
    print("你猜错啦！")

print("你与我的熟识度为"+ str(score) + "分")
