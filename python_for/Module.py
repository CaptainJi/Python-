#import time
import random
from time import sleep
from School.Student import Student


num=random.randint(1,1000)
#print(time.ctime())
print(num)
stu1=Student(input(),input())
stu1.talk()

sleep(5)
print('5')