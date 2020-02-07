# coding=utf-8
while True:
    a = int(input("请输入第一个数字"))
    sign = input("请输入运算方式，用+ - * / 符号表示")
    b = int(input("请输入第二个数字"))
    if sign == "+":
        print("运算结果是："+ str(a+b))
    elif sign == "-":
        print("运算结果是：" + str(a - b))
    elif sign == "*":
        print("运算结果是：" + str(a * b))
    elif sign == "/":
        print("运算结果是：" + str(a / b))

