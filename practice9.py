def open_account():
    print("새로운 계좌가 생성되었습니다")

# open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):   #저녁에 출금
    commission = 100 ##수수료 100
    return commission,balance-money-commission



balance = 0

balance = deposit(balance,1000)
# balance = withdraw(balance,2000)
# balance = withdraw(balance,500)
commission, balance = withdraw_night(balance,500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission,balance))


##기본값
def profile(name,age=17,main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
           .format(name,age,main_lang) )

profile("유재석",20,"파이썬")
profile("유재석")
profile("김태호")

#키워드값
def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(name="유재석",main_lang="파이썬",age=20)
profile(main_lang="자바",age=25,name="김태호")##순서가 뒤섞여있어도 괜찮음

##가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language):##가변인자
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석",20,"python","java","c","c++","c#","javascript")
profile("김태호",25,"kotlin","swift")


##지역변수 , 전역변수
gun=10
def checkpoint(soldiers) : 
    global gun #전역공간에 있는 gun사용
    gun=gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,2)
# gun = checkpoint_ret(20,2)
print("남은 총 : {0}".format(gun))


##퀴즈
from math import *
def std_weight(height,gender):
    if gender=="남자":
        weight=(height/100)*(height/100)*22
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height,weight))
        return round(weight,2)
    
    elif gender=="여자":
        weight=(height/100)*(height/100)*21
        print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height,weight))
        return round(weight,2)

std_weight(177.7,"남자")
