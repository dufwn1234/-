##list
##조세호가 몇번째칸에 타고 있는가
subway=["유재석","조세호","박명수"]
print(subway)
print(subway.index("조세호"))

##하하가 탓다
subway.append("하하")
print(subway) 

#w정형돈을 유재석 /조세호 사이에 채워보기
subway.insert(1,"정형돈")
print(subway) 

#지하철에 있는 사람을 꺼내기
print(subway.pop())
print(subway)  

# print(subway.pop())
# print(subway) 

# print(subway.pop())
# print(subway) 

##같은 이름의 사람이 몇명있는지
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬
num_list=[5,2,4,3,1,1,2,3]
num_list.sort()
print(num_list)

##정렬 뒤집기 (숫자뒤집기)
num_list.reverse()
print(num_list)

##모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형과 사용
num_list=[5,2,4,3,1]
mix_list=["조세호",20,True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

##########사전(목욕탕)
cabinet={3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) ##에러가나고 실행종료
print(cabinet.get(5))##에러가 나지 않음
print(cabinet.get(5,"사용가능")) 
print("hi")

print(3 in cabinet)
print(5 in cabinet)##False

cabinet={"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

##새손님
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet)

##간 손님
del cabinet["A-3"]
print(cabinet)

##key만출력
print(cabinet.keys())
## value만 출력
print(cabinet.values())

##쌍으로 출력
print(cabinet.items())

## 목욕탕 폐점
cabinet.clear()
print(cabinet)



