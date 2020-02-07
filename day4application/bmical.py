#coding=utf-8
height= float(input("请输入用户的身高 单位cm"))
height = height/100
weight= float(input("请输入用户的体重 单位kg"))
BMI = weight/(height*height)
if BMI<18.5:
    print("过轻")
    print("正常范围是"+ str(height*height*18.5) + "到"+ str(height*height*25))

elif 18.5<=BMI<25:
    print("正常")

elif 25<= BMI<28:
    print("过重")
    print("正常范围是" + str(height * height * 18.5) + "到" + str(height * height * 25))

elif 28<=BMI<32:
    print("肥胖")
    print("正常范围是"+ str(height*height*18.5) + "到"+ str(height*height*25))

else:
    print("严重肥胖")