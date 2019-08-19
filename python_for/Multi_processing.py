from time import sleep,ctime
import multiprocessing
from Multi_threading import Multi

#     for i in range(loop):
#         print('Start tallk:%s %s' %(content,ctime()))
#         sleep(2)
#
# def write(content,loop):
#     for i in range(loop):
#         print('Start write:%s %s' %(content,ctime()))
#         sleep(2)

process=[]
t1=multiprocessing.Process(target=Multi.talk,args=('Hello Big Pig!',2))
process.append(t1)

t2=multiprocessing.Process(target=Multi.write,args=('Life is short.You need Python!',2))
process.append(t2)
#执行线程
if __name__=='__main__':
    for t in  process:
        t.start()
    for t in process:
        t.join()
    print('All Thread end! %s' %ctime())