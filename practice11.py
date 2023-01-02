##파일 입출력("w"=쓰기용도)
# score_file=open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 10", file=score_file)
# score_file.close()


#"a"(내용추가)
# score_file=open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()


# #r(읽기전용)
# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.readline())#줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# # score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")

# score_file.close()    
# print(lines)

######피클
import pickle
# profile_file = open("profile.pickle","wb")##쓰기와 바이너리
# profile={"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)# profile에있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")##"rb"
# profile = pickle.load(profile_file)# file에있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# ####### with
# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))


# ##피클 사용 x
# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open ("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())


##퀴즈
for i in range(1,51):
    with open("{0}주차.txt".format(str(i),"w",encoding="utf8")) as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(i))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")

