# coding=utf-8
import random
while True:
    check = input("请问您是要添加单词表，还是进行猜词游戏。a 添加单词 b 猜词游戏")
    if check =='a':
        with open('wordlist.txt','a',encoding='utf-8') as file:
            addword = input("请输入您要添加的单词")
            file.write(addword+'\n')
    elif check=='b':
        with open('wordlist.txt','r',encoding='utf-8') as file:
            wordlist = file.readlines()
            #print(wordlist)
        word = random.choice(wordlist)
        length = len(word)
        list1 = [] #目标单词
        list2 = [] #当前的结果
        life = 6
        for i in range(0,length-1):
            list1.append(word[i])
            list2.append('_')
        #print(list1)
        print(list2)
        print()
        while list2 != list1 and life>0:
            userInput = input("请输入猜测的字母，每次输一个")
            if userInput in list1:
                for i in range(0,length-1):
                    if list1[i]==userInput:
                        list2[i] = userInput
                print(list2)
                print()
            else:
                life = life - 1
                print("您输入的字母不在这个单词中")
                print("您还剩下" + str(life)+"次的机会")
                print()

        if life>0:
            print("恭喜你！你成功完成了挑战！")
        else:
            print("很遗憾，你没有猜到最终的答案，这个单词是："+word)