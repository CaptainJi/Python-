import csv
# csv_file=csv.reader(open('stu_info.csv','r'))
# print(csv_file)
#
# for stu in csv_file:
#     print(stu)

stu=['Marry',28,'ChangSha']
stu1=['XiaoNan',31,'ChengDu']

out=open('stu_info.csv','a',newline='')
csv_write=csv.writer(out,dialect='excel')

csv_write.writerow(stu)
csv_write.writerow(stu1)

print('Write file over!')

csv_file=csv.reader(open('stu_info.csv','r'))
for line in csv_file:
    print(line)