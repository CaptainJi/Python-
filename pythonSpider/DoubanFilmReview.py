from urllib import request

def get_data():
    url='https://movie.douban.com/subject/26581837/comments?status=P'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    req=request.Request(url,headers=headers)
    response=request.urlopen(req)
    if response.getcode()==200:
        reault=response.read()
        print(reault)
        # return reault