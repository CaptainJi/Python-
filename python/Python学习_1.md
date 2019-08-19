
人生苦短，我用Python
==
---


" Life is short, you need Python" ——Bruce Eckel "

---




## Python是什么


是一种面向对象、解释型计算机程序设计语言，由“龟叔”（Guido van Rossum）于1989年圣诞节为打发无聊时间，而开发的一个新的脚本解释程序，至于为什么选中Python作为语言名字，是因为他是一叫Monty Python的喜剧团体的爱好者，第一个公开发行版发行于1991年。<br>
## 设计哲学
•	优雅<br>
•	明确<br>
•	简单<br>


## Python 为什么流行
•	代码量小<br>
•	维护成本低<br>
•	编程效率高<br>

编程语言排名：https://www.tiobe.com/tiobe-index/ <br>
## Python 可以用来做什么好玩的事情？
Python 最常用的应该就是写爬虫了吧，比较简单的应用就是爬取web网站的资源（图片，文字、链接等）
有些资深股民都是用 Python 抓取财经网站数据、并进行处理，然后输出可视化图表来帮助做决策。
人工智能机器学习方面应用，python有很多库很方便做人工智能，比如numpy, scipy做数值计算的，sklearn做机器学习的，pybrain做神经网络的。<br>

软件测试领域，自动化测试（Web端(python+selenium)和移动客户端python+appium）<br>

Python2.X 与Python3.X学哪个？<br>
个人推荐学习Python3.X,因为Python的2.x分支版本在2020年将停止更新，同时，Python 3将被定为该语言的未来发展方向。<br>
Python3针对Python2做了许多优化，特别是尤其是处理字符等。<br>




## Python安装配置

### Python下载
•	官网下载地址：https://www.python.org/downloads/windows/<br>
•	下载安装包：
1.	python-3.5.0-amd64（64位）.exe<br>
2.	python-3.5.0（32bit）.exe<br>

### Python安装
直接安装下载的安装包即可（建议安装在C盘根目录）<br>
安装完成后<br>
•	菜单栏查看目录<br>
•	磁盘路径查看<br>
•	调试运行-IDLE<br>
**pip安装Selenium**<br>
pip 是一个现代的，通用的 Python 包管理工具。提供了对 Python 包的查找、下载、安装、卸载的功能。<br>
**安装指定版本的Selenium**<br>
pip install selenium==2.48.0<br>
**查看当前包的版本信息**<br>
pip show selenium<br>
**卸载当前安装包**<br>
pip uninstall selenium<br>
**安装完成后路径**<br>
...\Lib\site-packages<br>
### PyCharm 安装
PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。<br>
官网下载地址（选择社区版）：<br>
 http://www.jetbrains.com/pycharm/download/#section=windows<br>

## 第一个Python程序

### print语句
```python
#打印字符串
print ("Hello,51zxw")
print("are","you","OK?")

#打印整数
print(500)
print(300+200)

#打印变量
name="51zxw"
print("hello,%s" %name)

width=30
print("width is %d " %width)
```
### input 语句

```Python
con=input("please input Content")
print("the input Content is %r" %con)
```
### 常用数据类型
#### 整数
```python
x=5
y=5
z=x+y
print (z)
```
#### 浮点数
```python
f=5.20
l=5.30
a=f+l
print(a)
```
#### 字符串
```python
str='hello 51zxw'
print(str)
```
#### 转义字符
```python
print("hello \n51zxw")

print('c:\\python35')

# my name is ‘Jack’ and “you”
print('My name is \'Jack\' and \”you\”')
```
#### 布尔值
```python
t=True
f=False
print(t and f)
```
#### 数组（List）
数组是一种有序的集合，可以随时添加和删除其中的元素。
##### 数组定义
```python
student=['Jack','Bob','Harry','Micle']
print(student)
```
##### 访问数组元素
用索引来访问list中每一个位置的元素，记得索引是从0开始的：
```python
student=['Jack','Bob','Harry','Micle']
print(student[0])
print(student[1])
print(student[-1])  #访问最后一个元素
```
注意： 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界。



##### 添加元素
```python
#末尾追加元素
student.append('51zxw')
print(student)

#指定位置添加元素
student.insert(0,'hello')
print(student)
修改元素
student[0]='No.1'
print(student)
删除元素
#删除末尾元素
student.pop()
print(student)

#删除指定位置元素
student.pop(1)
print(student)
```
#### 元组（Tuple）
Python的元组与列表类似，不同之处在于元组的元素一旦定义就不能修改。 元组使用小括号，列表使用方括号。 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。<br>
```python
course=('Chinese','Math','English','computer')
print(course)
print(course[0])
print(course[1:3])
print(len(course))
要定义一个只有1个元素的元组，则需要在元素后面加逗号，用来消除数学歧义
t = (1,)
返回元组最大的值
score=(78,90,88,67,78)
print(max(score))
```
#### 字典(Dictionary)
字典是另一种可变容器模型，且可存储任意类型对象。 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号{}中 ,格式如下所示：<br>
```python
d = {key1 : value1, key2 : value2 }
```
键必须是唯一的，但值则不必。 值可以取任何数据类型，但键必须是不可变的。
#### 定义访问字典
```python
student={1:'Jack',2:'Bob',3:'Marry',4:'Micle'}
print(student[3])
```
#### 添加元素
```python
#增加新的键值对
student[5]='51zxw'
print(student)
```
#### 修改元素
```python
#修改字典
student[2]='Harry'
print(student)
```
#### 删除字典
```python
#删除某一个键值对
del student[1]
print(student)


#清空字典全部内容
student.clear()
print(student)

#删除字典
del student
```
### 条件判断
Python 编程中 if 语句用于控制程序的执行，基本形式为：<br>
&emsp;if 判断条件：<br>
    &emsp;&emsp;&emsp;&emsp;执行语句……<br>

else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句

&emsp;if 判断条件：<br>
    &emsp;&emsp;&emsp;&emsp;执行语句……<br>
&emsp;else：<br>
    &emsp;&emsp;&emsp;&emsp;执行语句……<br>

##### 案例1：<br>
根据分数来判断学生成绩是否为优秀，80分及以上为优秀，评级为A。<br>
```python
score=80
if score>=80:
    print("Score is A")
else:
    print("score is not A")
注意：print 语句要注意缩进，不要Tab和空格混用，否则回编译报错。
案例2：成绩80分以上为评级A，60~79分为B, 60分以下为C
score=90
if score>=80:
    print("Score is A")
elif score>=60:
    print("Score is B")
else:
    print("Score is C")
```
Tips：elif是else if的缩写，完全可以有多个elif


### 循环语句
循环语句允许我们执行一个语句或语句组多次，Python提供了for循环和while循环（在Python中没有do..while循环）<br>
#### for循环
##### 案例1：<br>
将Student 数组值全部打印出来<br>
```python
student=['Jack','Bob','Marry','Micle']
for stu in student:
    print(stu)
```
##### 案例2：
计算1+2+3+...10的值<br>
Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(10)生成的序列是从0开始小于10的整数。<br>
```python
sum=0
for i in range(11):
    sum=sum+i
print(sum)
```
#### While循环
while循环，只要条件满足，就不断循环，条件不满足时退出循环。
```python
n=10
while n>0:
    n=n-1
    print(n)
print('Game over!')
```


## Python猜数小游戏
【游戏规则】生成一个指定范围的随机数（如：1-100），然后玩家输入数值猜答案，屏幕会根据玩家输入的数字给出大小提示，一直到玩家猜出准确答案则游戏胜利并结束。<br>
```python
import  random
answer=random.randint(1,100)
n=int(input("Please input num: "))
while n!=answer :
      if n>answer:
          n = int(input("Num is Big! Please Continue input: "))
      elif n<answer:
          n = int(input("Num is small! Please Continue input: "))

print("You Win the game!")
```
