# Class2.py
# 클래스 형식 정의 ( 쿠키틀, 템플릿)
class Person:
    #위치를 잘 보자.
    num_person = 0
    #초기화 메서드(멤버 변수 초기화를 담당)
    def __init__(self):
        #인스턴스에 소속된 인스턴스 멤버 변수
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))
                    # ------------------------------------ class body

p1= Person()
p2= Person()
p3= Person()

print( "인스턴스의 갯수 : ", Person.num_person)