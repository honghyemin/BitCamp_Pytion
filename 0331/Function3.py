# Function3.py
# 가변인자를 처리하는 경우(갯수가 정해지지 않은 경우)
def union(*ar):
    #지역변수
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 함수를 호출
print( union("HAM", "EGG"))
print( union("HAM", "EGG", "SPAM"))

print("----------------------------------------------------------")
# 정의되지 않은 인자
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str              # 위의 네 줄이 userURIBuilder의 body

# 호출
print( userURIBuilder("bitCamp", "80", id="kim", mane="mike"))
print( userURIBuilder("bitCamp", "80", id="kim", mane="mike", age="30"))


# 람다함수 ( 이름이 없는 임시 함수)
g = lambda x,y:x*y
print( g(3,4))
print( g(5,6))
print( (lambda x:x*x)(3))
print( globals())
