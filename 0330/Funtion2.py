# Funtion2.py
# 전역변수와 지역변수(LGB)
x = 1
def func(a):
    return a+x

# 함수 호출
print( func(1))

# 지역변수가 있는 경우
def func2(a):
    x = 2
    return a+x

# 함수 호출
print( func2(1))


# 불변형식을 함수 내부에서 변경하는 경우
g = 1 
def testScope(a) :
    #global g
    g = 2
    return a + g

# 호출
print( testScope(1))
print("전역변수 g:", g)







# 기본값이 있는 경우
def times(a=10, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자(파라메터 명을 명시하는 경우)
def connectURI(server, port):
    str = "http://" + server + ":" + port
    return str


# 호출
print( connectURI("bitCamp", "80"))
print( connectURI(port="80", server="bitCamp"))

