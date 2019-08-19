from urllib import request
import json
from openpyxl import Workbook

#获取数据
def get_data(url):
    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'}
    req=request.Request(url,headers=headers)
    response=request.urlopen(req)
    if response.getcode()==200:
        return response.read()
#处理数据
def parse_data(html):
    data=json.loads(html)

    comments=[]
    for item in data['data']['comments']:
        comment={
            'id':item['id'] if 'id' in item else'',
            'nick':item['nick'] if 'nick' in item else '',
            'content':item['content'] if 'content' in item else '',
            'score':item['score'] if 'score' in item else '',
            # 'startTime':item['startTime'] if 'startTime' in item else ''
        }

        comments.append(comment)
    # print(jsonpath(data,"$..comments[*].id"))
    # print(comments)
    return comments

def save_to_txt():
    cont=0
    while cont<1000:
        url=('http://m.maoyan.com/review/v2/comments.json?movieId=342903&userId=-1&offset=%d&limit=15&ts=0&type=3'%cont)
        html=get_data(url)
        comments=parse_data(html)
        cont+=15
        for item in comments:
            with open('comments.txt',mode='a',encoding='utf-8') as f:
                f.write(str(item['id'])+','+item['nick']+','+item['content']+','+str(item['score'])+','+'\n')




if __name__=='__main__':
    # url='http://m.maoyan.com/review/v2/comments.json?movieId=342903&userId=-1&offset=0&limit=15&ts=0&type=3'
    # get_data(url)
    save_to_txt()
    # save_to_txt()