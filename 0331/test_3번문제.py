# 3번문제.py
# 파이썬에서 a = [1,2,3] 이라는 형태의 코드를 b = a에 대입할 때 
# 얕은 복사로 처리하는 코드와 깊은 복사로 처리하는 코드를 둘 다 작성하고 비교해서 설명해보세요. 

# 얕은복사
print("---------얕은 복사--------")
a = [1, 2, 3]
b = a
a[0] = 7
print(a)
print(b)



# 깊은 복사
print("---------깊은 복사--------")
a = [1, 2, 3]
b = a[:]
a[0] = 7
print(a)
print(b)
