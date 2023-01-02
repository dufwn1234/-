#탈출문자
print("백문이 불여일견 백견이 불여일타")

print("백문이 불여일견\n백견이 불여일타")##\n줄바꿈

print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")##\",\'
print("저는 \'나도코딩\'입니다.")

##\\=문장 내에서는 하나의\로 취급
print("C:\\Users\\dufwn\\Desktop\\python")

##\r=커서를 맨앞으로 이동
print("Red Apple\rpine" )##pineapple

##\b=백스페이스(한글자 삭제)
print("Redd\b Apple")

##\t=tab
print("Red\tApple")


##퀴즈
##a="http://youtube.com"
a="http://naver.com"
b=a[7:] ## a=a.replace("http://","")
print(b)
b=b[:b.find(".")]
print(b)
password = b[:3] + str(len(b)) + str(b.count("e")) + "!"
print("생성된 비밀번호 : " + b[:3] + str(len(b)) + str(b.count("e")) + "!")
print("{0}의 비밀번호는 {1}입니다.".format(a,password))
##print(f"{a}의 비밀번호는 {password}입니다.")
