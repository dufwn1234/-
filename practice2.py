##슬라이싱
jumin="970104-1234567"

print("성별 = ", jumin[7])
print("연 = ", jumin[0:2])
print("월 = ", jumin[2:4])
print("일 = ", jumin[4:6])
print("생년월일 = ", jumin[0:6])
print("생년월일 = ", jumin[:6])##0을 제외해도됨

print("뒤 7자리 = ", jumin[7:14])
print("뒤 7자리 = ", jumin[7:])##맨뒤까지 할꺼면 숫자 안써도 됨
print("뒤 7자리 (뒤에서부터) = ", jumin[-7:])##맨 뒤에서 부터 
