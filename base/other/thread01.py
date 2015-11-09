import urllib2 

urls=['http://www.baidu.com','http://www.douban.com']
result=map(urllib2.urlopen,urls)
print result

print '\n--------------------------------'

result=[]
for url in urls:
    result.append(urllib2.urlopen(url))

print result


