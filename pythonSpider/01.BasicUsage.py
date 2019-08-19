# 导入urllib中的request模块，用来发送http/https请求
from urllib import request
# 导入BeautifulSoup4中的BeautifSoup模块，用来处理数据
from bs4 import BeautifulSoup
#导入PyMySQL操作MySQL
import pymysql
#导入Openpyxl操作Excel
from openpyxl import Workbook


# 获取数据
def get_data():

    for page in range(1,8):
        url = 'https://search.51job.com/list/220200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2,{}.html'.format(page)

    # 创建Request对象,指定url和请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}  # 请求头，模拟浏览器发出请求
        req = request.Request(url, headers=headers)
        response = request.urlopen(req)

        # print(type(response))#获取Response类型
        # print(response.getcode())#获取响应状态码
        # print(response.info())#获取响应信息
        if response.getcode() == 200:  # 如果响应状态码为200
            data = response.read()  # 读取响应结果
            # print(type(data))
            data = str(data, encoding='gbk')
            # print(data)
            # 将数据写入文件中
            with open('index.html', mode='a', encoding='gbk') as f:
                f.write(data)
        page += 1

# 解析数据

def parss_data():
    with open('index.html', mode='r', encoding='gbk') as f:
        html = f.read()

    # 创建BeautifSoup实例，解析html数据
    bs = BeautifulSoup(html, 'html.parser')  # 指定使用html解析器parser

    '''
    查找数据
    '''
    # 1.find()方法，获取第一个匹配的标签

    # div=bs.find('div')
    # print(div)

    # 2.find_all()方法，获取所有匹配的标签

    # div=bs.find_all('meta')
    # print(div[0])
    # print(bs.find_all(id='hello'))#根据id返回，返回的是集合
    # print(bs.find_all(class_ ='itany'))#根据class获取

    #3.select()方法，使用CSS选择器来获取元素
    # print(bs.select('#Hello')[0]) #   “#”代表取id
    # print(bs.select(' .itany') #   “.”代表取class 注意.前面的空格
    # print(bs.select('p#world span')) #取span
    # print(bs.select('[title]')) #取title
    # print(bs.select('#hello')[0].get_text().strip())#get_text()获取Tag中的文本,strip()只取字符或使用get_text(strip=True)只取字符

    #获取职位信息
    divs=bs.select('#resultList .el')
    result=[]
    for div in divs[1:]:
        title=div.select(' .t1')[0].get_text(strip=True)
        company=div.select(' .t2')[0].get_text(strip=True)
        addr=div.select(' .t3')[0].get_text(strip=True)
        salary=div.select(' .t4')[0].get_text(strip=True)
        pubDate=div.select(' .t5')[0].get_text(strip=True)
        # print(title,company,addr,salary,pubDate)
        row={
            'title':title,
            'company':company,
            'addr':addr,
            'salary':salary,
            'pubDate':pubDate
        }
        result.append(row)
    return result

#存储数据到MySQL

def save_to_mysql(data):
    config={
        'host':'localhost',
        'port':3306,
        'user':'root',
        'password':'root',
        'database':'python',
        'charset':'utf8'
    }
    conn=pymysql.connect(**config)
    cursor=conn.cursor()
    sql='''
        insert into t_job
            (title, company, addr, salary, pubDate)
        values 
            (%(title)s,%(company)s,%(addr)s,%(salary)s,%(pubDate)s)
    '''
    cursor.executemany(sql, data)
    conn.commit()

    cursor.close()
    conn.close()

#存储数据到Excel

def save_to_excel(data):
    #创建工作薄workbook
    book=Workbook()
    #创建工作表
    sheet=book.create_sheet('信息',0)
    #向工作表中添加数据
    sheet.append(['职位名','公司名','工作地点','薪资','发布时间'])
    for item in data:
        row=[item['title'],item['company'],item['addr'],item['salary'],item['pubDate']]
        sheet.append(row)

    #输出保存
    book.save('job.xlsx')

if __name__ == '__main__':
    # get_data()
    # print(parss_data())
    # save_to_mysql(parss_data())
    save_to_excel(parss_data())