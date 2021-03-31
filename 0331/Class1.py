# Class1.py
# 클래스 형식 정의 ( 쿠키틀, 템플릿)
class Person:
    #초기화 메서드(멤버 변수 초기화를 담당)
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))
                    # ------------------------------------ class body
# 인스턴스 생성
p1 = Person() # ()가 초기화 메서드와 맵핑되어있음
p2 = Person()
p2.name = "전우치"

p1.print() # body에 있는 것을 불러줌
p2.print()