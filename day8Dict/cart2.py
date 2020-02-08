# coding = utf-8
items = {'1000':['苹果',8,'1000',"看起来很好吃"],'1001':['香蕉',5,'1001',"富含维生素，产自北京"],'1002':['口罩',10,'1002',"N95高度防护口罩"]}
purchased = {}
totalPrice = 0
while True:
    print("请输入您的指令：")
    print()
    print("a. 查看全部的商品")
    print("b. 商品详情")
    print("c. 购买指定货品")
    print("d. 结账")
    print()
    userInput = input()
    if userInput=='a':
        for i in items:
            print("产品名： "+items[i][0]+" 编号为： "+items[i][2])

    if userInput=='b':
        for i in items:
            print("产品名： "+items[i][0]+" 编号为： "+items[i][2])
        ans = input("请输入产品的4位编号")
        print("该产品的介绍为："+ items[ans][3]+" 产品单价："+str(items[ans][1]))

    if userInput =='c':
        money=0
        for i in items:
            print("产品名： "+items[i][0]+" 编号为： "+items[i][2])
        num = input("请输入要购买的产品编号")
        num2 = int(input("请输入购买的数量"))
        money = money + num2 * items[num][1]
        totalPrice = totalPrice + money
        purchased[num] = [items[num][0], num2, money]
        print("购买成功！")
        print()

    if userInput == 'd':
        print("这是您本次购物的清单：")
        for i in purchased:
            print("品名：" + purchased[i][0] + " 数量：" + str(purchased[i][1]) + " 总价：" + str(purchased[i][2]))
        print("总计价格为：")
        print(totalPrice)
        break

print("感谢购物！欢迎下次光临!")