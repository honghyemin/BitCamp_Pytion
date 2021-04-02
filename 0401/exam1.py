# exam1.py
class Person:
    num_person = 0
    def __init__(self):
        self.name = "defalut name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
print("숫자 : {0}".format(Person.num_person))

