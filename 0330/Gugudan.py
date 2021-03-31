# Gugudan.py
# 외곽에 있는 반복문을 Outer
for x in [2,3,4,5,6] :
    print("--{0}단".format(x))
    # 내부에 있는 반복문을 Inner
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

# 삼각형을 출력
for i in [1,2,3,4,5,6,7,8,9,10] :
    print("*" * i)

# 리스트 컴프리헨션
lst = [1,2,3,4,5,6,7,8,9,10]
result = [i**2 for i in lst if i>5]
print(result)

tp = ("apple", "orange", "kiwi")
print([len(i) for i in tp])


# 딕셔너리
d = { 100:"apple", 200:"kiwi", 300:"orange"}
print([v.upper() for v in d.values()])


# 반복문에서 걸러내기를 할 경우
L = [10, 20, 30]
iterL = filter(None, L)
for i in iterL:
    print(i)

print("====필터링====")
# 필터링하는 함수 정의
def getBigerthan20(i):
    return i>20

iterL = filter(getBigerthan20, L)
for i in iterL:
    print(i)

