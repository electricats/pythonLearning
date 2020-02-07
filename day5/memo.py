#coding=utf-8
a = input("请输入您需要储存，还是查找密码？a.代表储存，b.代表查找")
if(a=="a"):
    webname = input("请输入网站的名字")
    pw = input("请输入该网站的密码")
    with open('pw.txt','a',encoding='utf-8') as file:
        file.write(webname + "的密码是： "+pw+ "\n")

if(a== "b"):
    webname = input("请输入想要搜索的网站名")
    with open('pw.txt','r',encoding='utf-8') as file:
        check = 0
        for content in file.readlines():
            if webname in content:
                print(content)
                check = 1
        if check == 0 :
            print("未查找到该数据！")