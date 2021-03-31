# Function4.py

for char in "abc":
    print(char)

for item in [1,2,3]:
    print(item)

# 내부에서는 이렇게 구현(저수준)
s = "abc"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))


# 문자열을 뒤집어서 리턴하는 함수
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

# 호출
for char in reverse("gold"):
    print(char)

print("--------------------------------------")
# 좀 더 쉬운 예제(yield)
def abc():
    s = "abc"
    for char in s :
        yield char # yield : 생성-> 추출 -> 반환

# 호출
for char in abc():
    print(char)

