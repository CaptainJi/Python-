from urllib import request
from openpyxl import Workbook
import json

#获取数据
def get_data():
    url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=400&page_start=0'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    req=request.Request(url,headers=headers)
    response=request.urlopen(req)
    if response.getcode()==200:
        reault=response.read()
        # print(response.read())
        return reault

#解析数据
def parse_data(html):
    #讲字符串形式的json转换为dict字典
    result=[]
    data=json.loads(html)
    movies = data['subjects']
    for movie in movies:
        title=movie['title']
        rate=movie['rate']
        row={'title':title,'rate':rate}
        result.append(row)
    return result

#存储数据到Excel

def save_to_excel(data):
    #创建工作薄workbook
    book=Workbook()
    #创建工作表
    sheet=book.create_sheet('影评',1)
    #向工作表中添加数据
    sheet.append(['电影名','豆瓣评分'])
    for item in data:
        row=[item['title'],item['rate']]
        sheet.append(row)
    # print(row)
    #输出保存
    book.save('job.xlsx')

if __name__=='__main__':
    save_to_excel(parse_data(get_data()))