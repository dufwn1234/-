##튜플
menu=("돈까스","치즈까스")
print(menu[0])
print(menu[1])

name="김종국"
age=20
hobby="코딩"
print(name,age,hobby)

(name,age,hobby)=("김종국",20,"코딩")
print(name,age,hobby)


##세트 (set,집합)
##중복안됨,순서없음
my_set={1,2,3,3,3}
print(my_set)

java={"유재석","김태호","양세형"}
python=set(["유재석","박명수"])

##교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

##합집합
print(java | python)
print(java.union(python))

##차집합(java는 할수있지만 python은 할수없는)
print(java - python)
print(java.difference(python))

##python을 할줄아는 사람이 늘어남
python.add("김태호")
print(python)

##java를 할줄까먹음
java.remove("김태호")
print(java)

##자료구조의 변경
##커피숍
menu={"커피","우유","주스"}
print(menu,type(menu))

menu=list(menu)
print(menu,type(menu))


menu=tuple(menu)
print(menu,type(menu))

menu=set(menu)
print(menu,type(menu))


# ########퀴즈
# from random import *
# lst=[1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))
from random import *
# a=range(1,21) ##1부터 20
# a=list(a)
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(a)
shuffle(a)
b=sample(a,1)
print(b)
a=set(a)
b=set(b)
c=a-b
d=sample(list(c),3)
print('''
-- 당첨자 발표--
치킨 당첨자 : {0}
커피 당첨자 : {1}
-- 축하합니다 --
'''.format(list(b)[0],d))