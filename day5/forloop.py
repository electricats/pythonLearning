ans = 1
a = int(input("请输入需要连乘的结果"))
for num in range(1,a+1):
    print(num)
    ans = ans * num

print("从1加到"+str(a)+"的结果为:"+ str(ans))