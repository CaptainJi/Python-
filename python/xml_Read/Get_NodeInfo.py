from xml.dom import minidom

#打开xml文件
dom=minidom.parse('Class_info.xml')
root=dom.documentElement

# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)

name=root.getElementsByTagName('name')
age=root.getElementsByTagName('age')
city=root.getElementsByTagName('city')

for i in range(4):
    print(name[i].firstChild.data)
    print(age[i].firstChild.data)
    print(city[i].firstChild.data)
