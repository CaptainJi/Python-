def Max_num(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else :
        return a

result=Max_num(a=input("请输入第一个数字"),b=input('请输入第二个数字'))
print(result)