class Person:
    name = "myName"
    age = ""

    def __init__(s, name, age):
        s.name = name
        s.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


class Student(Person):
    school = ''
    number = ''

    def __init__(s, name, age):
        super().__init__(name, age)

    def __init__(s, school, number):
        s.school = school
        s.number = number

    def sayHello(x):
        print('Hello ' + x.name)


p1 = Student("school", 236)
p1.sayHello()
