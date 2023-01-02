##표준 입출력
print("python","java",sep=" vs ")
print("python","java","javascript",sep=" vs ")


print("python","java",sep=",")
print("무엇이 더 재미있을까요?")

print("python","java",sep=",",end="?")##end는 문장의 끝 부분에 ?를 넣어라
print("무엇이 더 재미있을까요?")

import sys
print("python","java",file=sys.stdout)
print("python","java",file=sys.stderr)

#시험성적
scores = {"수학":0,"영어":50,"코딩":100}
# print(scores)
for subject, score in scores.items():
    # print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":")


# #은행 대기순번표
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3))

# answer=input("아무 값이나 입력하세요 : ")
# print("입력하신 값은" + answer + "입니다.")


#####다양한 출력포맷
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#양수일때는 +표시, 음수일땐는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽정렬을 하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))
#3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000000))
#3자리마다 콤마를 찍어주기,+-부호도 붙이기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))
#3자리마다 콤마를 찍어주기,+-부호도 붙이기,자릿수 확보하기
#돈이 많으면 행복하니까 빈자리는 ^로 채우기
print("{0:^<+30,}".format(-100000000000000)) 
#소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))# 소수점 둘째자리까지 표시(셋째에서 반올림)


