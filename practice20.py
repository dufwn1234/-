# import travel.thiland
# trip_to = travel.thiland.ThailandPackage()
# trip_to.detail()

# from travel.thiland import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# ##__all__
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# # trip_to.detail()
# trip_to = thiland.ThailandPackage()
# trip_to.detail()



# ##모듈 직접 실행
# from travel import *
# trip_to = thiland.ThailandPackage()
# trip_to.detail()


##패키지, 모듈 위치
# from travel import *
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thiland))

# trip_to = thiland.ThailandPackage()
# trip_to.detail()


# ### pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# ##내장함수
# #input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요? ")
# print("{0}은 아주 좋은 언어 입니다.".format(language))

##dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 갖고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# # print(dir(random))
# lst = [1,2,3]
# print(dir(lst))

# name="jim"
# print(dir(name))

##외장 함수
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py인 모든 파일

# #os : 운영 체제를 제공하는 기본 기능
# import os
# # print(os.getcwd())

# # folder = "sample_dir"

# # if os.path.exists(folder):
# #     print("이미 존재하는 폴더")
# #     os.rmdir(folder)
# #     print(folder,"돌더를 삭제하였습니다.")

# # else:
# #     os.makedirs(folder) #폴더생성
# #     print(folder,"폴더를 생성 하였습니다.")
# print(os.listdir())


# #time : 시간관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
 

import datetime
# print("오늘 날짜는 " ,datetime.date.today())

#####timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td=datetime.timedelta(days=100)
print("우리가 만난지 100일은 ", today + td)