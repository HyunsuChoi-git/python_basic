
from winreg import ExpandEnvironmentStrings

class ZeroNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num2 == 0 :
        raise ZeroNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except ZeroNumberError as selfErr:
    print("오류발생!! ["+selfErr.msg+"]")
finally:
    print("빠잉")