f=open('stu_info.txt','r')
lines=f.readlines()
print (lines)

for line in lines:
    print(line.split(',')[0])