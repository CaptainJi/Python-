
import random
#生成随机数
answer = random.randint(1,100)
#输入数值
n = int(input('请输入1-100的数值：'))
#判断数值
while n!=answer:
    if n>answer:
        n = int(input('您输入的数值大了，请继续输入数值：'))
    elif n<answer:
        n = int(input('您输入的数值小了，请继续输入数值：'))
#显示结果
print('数值正确')

a = input('输入数值a')
b = input('输入数值b')
