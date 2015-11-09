#xiancheng pool
import urllib2 
from multiprocessing.dummy import Pool as ThreadPool
urls=['http://www.baidu.com/s?wd=reboot',
    'http://www.baidu.com/s?wd=reboot+python',
    'http://www.baidu.com/s?wd=reboot+devops',
    'http://www.baidu.com/s?wd=reboot+ops',
    'http://www.baidu.com/s?wd=reboot+gko_pool',]
    
pool=ThreadPool(4)

results=pool.map(urllib2.urlopen,urls)
print results
pool.close
pool.join()


