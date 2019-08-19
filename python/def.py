class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s" % (name, city))

    def talk(self):
        print('Hello,world!')

# 生成实例对象
stu1=Student('Jack','Beijing')
stu1.talk()
stu2=Student('Harry','Shanghai')
stu2.talk()