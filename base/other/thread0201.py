#xiancheng pool
import urllib2 
from Trace import trace
from multiprocessing.dummy import Pool as ThreadPool
urls=['http://www.baidu.com/s?wd=reboot',
    'http://www.baidu.com/s?wd=reboot+python',
    'http://www.baidu.com/s?wd=reboot+devops',
    'http://www.baidu.com/s?wd=reboot+ops',
    'http://www.baidu.com/s?wd=reboot+gko_pool',]

@trace
def gethtml(urls):
    res=urllib2.urlopen(urls)
    html=res.read()
    return html
 
pool=ThreadPool(4)
results=pool.map(gethtml,urls)
pool.close
pool.join()
print results