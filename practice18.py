##예외처리
# try:

#     print("나누기 전용 계산기")
#     nums=[]
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))

# except ValueError:
#     print("에러! 잘못된값을 입력하셨습니다.")

# except ZeroDivisionError as err:
#     print(err)

# except Exception as err :
#     print("알수없는 에러가 발생하였습니다.")
#     print(err)


# ####에러발생시키기
# try :
#     print("한자리 전용 나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된값을 입력하셨습니다. 한자리 숫자만 이용하세요")
 
##사용자 정의 예외처리
# class Bignumbererror(Exception):
#     def __init__(self, msg) :
#         self.msg=msg

#     def __str__(self):
#         return self.msg

# try :
#     print("한자리 전용 나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise Bignumbererror("입력값 : {0}, {1}".format(num1,num2))
#     print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된값을 입력하셨습니다. 한자리 숫자만 이용하세요")
# except Bignumbererror as err:

#     print("잘못된값을 입력하셨습니다. 한자리 숫자만 이용하세요")
#     print(err)

# ##finally
# class Bignumbererror(Exception):
#     def __init__(self, msg) :
#         self.msg=msg

#     def __str__(self):
#         return self.msg

# try :
#     print("한자리 전용 나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise Bignumbererror("입력값 : {0}, {1}".format(num1,num2))
#     print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된값을 입력하셨습니다. 한자리 숫자만 이용하세요")
# except Bignumbererror as err:

#     print("잘못된값을 입력하셨습니다. 한자리 숫자만 이용하세요")
#     print(err)

# finally:
#     print("계산기를 이용해주셔서 감사합니다.")


##퀴즈
chicken=10
waiting=1
class SoldOutError(Exception):
    def __init__(self, msg) :
        self.msg=msg

    def __str__(self):
        return self.msg


while(True):
    try:
        print("[남은 치킨] : {0}".format(chicken))
        order = int(input("치킨 총 몇마리 주문하시겠습니까? "))
    

        if order > chicken:
            print("재료가 부족합니다.")
        elif order<1 :
            raise ValueError
            
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
            .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken==0 :
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")

    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError as err:
        print(err)
        break
    

            