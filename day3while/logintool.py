# coding=utf-8
successed = "no"  #这是个开关
while successed == "no":
    username = input("Please input your username/请输入你的用户名")
    pw = input("Please input your password/请输入你的密码")
    if username == "will":
        if pw == "1234":
            print("欢迎登陆, "+ username)
            successed = "yes"
        else:
            print(username+ "你是不是输错了密码？")

    elif username == "tom":
        if pw == "abcd":
            print("欢迎登陆, " + username)
            successed = "yes"
        else:
            print(username+ "你是不是输错了密码？")
    else:
        print("你是不是连用户名都忘啦！")
print("欢迎进入xxx系统，请开始您的操作吧！")
