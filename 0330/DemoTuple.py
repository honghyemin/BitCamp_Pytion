# DemoTuple.py
# 함수를 정의
def calc(a,b) :
    return a+b, a*b

# 함수를 호출(call)
# 디버깅 모드로 실행할 때 중지점(Break Point)
result = calc(3,4)
print(result)
print(result[0], result[1])
