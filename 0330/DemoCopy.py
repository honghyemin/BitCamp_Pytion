# DemoCopy.py
print( 1 < 2 ) 
isRight = True
print(type(isRight))
print( 1 != 2)
print( 1 == 2)
print( True and True and False)
print( True or False or False)

#파이썬이 참, 거짓을 판단하는 근거
print( "=======참, 거짓=======")
print( bool(0))
print( bool(1))
print( bool(""))
print( bool("demo"))
print( bool(None))
print( bool([]))
print( bool([1, 2, 3]))

# 얕은 복사, 깊은 복사
print("====== 얕은 복사 =======")
a = [1,2,3]
b = a
a[0] = 38
print( id(a), id(b))
print(a)
print(b)

print("====== 깊은 복사 =======")
a = [1,2,3]
b = a[:]
a[0] = 38
print( id(a), id(b))
print(a)
print(b)

# 리스트 형식이 아닌 경우
# 특정 블럭을 주석 처리 : crtl + /
import copy
a = [100, 200, 300]
b = copy.deepcopy(a)
a[0] = 101
print( id(a), id(b))
print(a)
print(b)
