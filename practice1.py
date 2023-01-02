print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
#####


print('풍선')
print("나비")
print("ㅋ"*9)
########
###참/거짓

print(5<10)
print(5>10)
print(True)
print(False)
print(not True)
print(not 5>10)


###변수 (애완동물 소개)
animal="강아지"
age=4
name="연탄이"
is_adult=age>=3
hobby="산책"

print("우리집"+ animal+"의 이름은" + name +"예요")
##hobby="공놀이"
print(name, "는 " , age , "살이며," , hobby ,"을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))

##주석 '''  ㅇㄴㅁㅇㄴㅁㅇㅁㅇㄴㅁ  '''
##퀴즈
station="사당"
print(station,"행 열차가 들어오고 있습니다")
station="신도림"
print(station,"행 열차가 들어오고 있습니다")
station="인천공항"
print(station,"행 열차가 들어오고 있습니다")

##연산자
print(2**3)
print(5%3) ## 나머지 표현
print(10//3) ##몫을 표현
print(2!=3)
print((3>0) & (3>5))
print((3>0) | (3>5))

##간단한 수식
number=2*3+4
print(number)
number += 2
print(number)
number %= 2
print(number)

##숫자 함수
print(abs(-5))
print(pow(2,5))
print(round(3.14))
print(min(4,5,6)) 

from math import *
print(floor(3.14))
print(ceil(3.14))
print(sqrt(16))

##랜덤함수
from random import *
print(random()) ## 0.0 이상 1.0미만의 임의의 값
print(random()*10) ## 0.0 이상 10.0미만의 임의의 값
print(int(random()*10)) ## 0 이상 10미만의 임의의 값
print(int(random()*10)+1)## 0 이상 10이하의 임의의 값

print(int(random()*45)+1)##1~45의 값 생성
print(randrange(1,46))##1~45의 값 생성(46미만)
print(randint(1,45))

##퀴즈2
from random import *
a=randint(4,28)
print("오프라인 스터디 모임 날짜는 매월",a,"일로 선정되었습니다")

##문자열
sentence='나는 소년입니다'
print(sentence)
sentence2="파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

