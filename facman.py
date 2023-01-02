import random
a=["apple","banana","orange"]
b=random.choice(a)
# c = len(b)
# print("_ "*c)
letters=""# 사용자로부터 받은 모든 알파벳

while True:
    succeed = True
    for i in b:
        if  i in letters:
            print(i,end=" ")
        
        else :
            print("_",end=" ")
            succeed = False
    if succeed:
        print("\nsuccess")
        break

    letter=input("\n입력하세요 : ")
    if letter not in letters:
        letters += letter


    if b in letter:
        print("collect")
    else: 
        print("wrong")





