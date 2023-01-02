##continue break
absent=[2,5]
no_book=[7]
for student in range(1,11):
    if student in absent:
        continue
    
    if student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))



####한줄 for
#출석번호가     1 2 3  4  5
#앞에 100을 붙이기로함 101 102 103 104
# students=[1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

##학생이름을 길이로 변환
students = ["Iron man","Thor","I am groot"]
students = [len(i) for i in students]
print(students)

#대문자 변환
students = ["Iron man","Thor","I am groot"]
students = [i.upper() for i in students]
print(students)

#####퀴즈
from random import *
e=0
for i in range(1,51):
    b = int(random()*50)+5
    if 5<=b<=15:
        c="O"
    else:
        c=" "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(c,i,b))
    if c=="O":
        e=e+1
print("총 탑승 승객 : {0}분".format(e))

