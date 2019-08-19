class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print('My name is %s and come from %s'%(name,city))

    def talk(self):
        print('Hello World!')

stu1=Student(input('请输入'),input('请输入城市'))
stu1.talk()