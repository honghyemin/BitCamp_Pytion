# Function1.py
# 함수를 정의
def times(a,b):
    return a*b

# 함수를 호출
print( times(3,4))

# 값을 반환하지 않는 경우
def setValue(newValue):
    x = newValue

# 호출
result = setValue(5)
print(result)


# 디버깅 연습
def intersect(prelist, postlist):
    #지역변수(리스트)
    retList = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in retList: #not in 포함되어있지 않으면
            retList.append(x)
    return retList

# 호출(디버깅할 때 중지점, Break Point)
print( intersect("HAM", "SPAM"))


# 불변형식 ( 정수, 실수, 문자열, 튜플)
a = 1.2
print( id(a))
a = 2.3
print( id(a))

# 가변형식 ( 리스트, 딕셔너리)
lst = [1,2,3]
print("list:", id(lst))
lst.append(4)
print("list:", id(lst))

# 가변형식을 매개변수로 넘기는 경우
def change(x):
    x[0] = "H"

# 함수를 호출(가변형식을 Pass By Reference로 넘긴 경우 참조가 복사됨)
wordlist = ["J", "A", "M"]
change(wordlist)
print("함수 호출 후:", wordlist)


# 가변형식을 매개변수로 넘기는 경우
def change(x):
    #깊은 복사(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부 :", x1) # 원본이 바뀐 것이 아니라 복사본이 생긴 것.

# 함수를 호출(가변형식을 Pass By Reference로 넘긴 경우 참조가 복사됨)
wordlist = ["J", "A", "M"]
change(wordlist)
print("함수 호출 후:", wordlist) # 원본 wordlist는 변경이 안됨.