filter
给定一个对象的序列和一个“过滤”函数，每个序列元素都通过这个过滤器进行筛选， 保留函数返回为真的的对象。
filter 函数为已知的序列的每个元素调用给定布尔函数。每个filter 返回的非零（true)值元素添加到一个列表中。 返回的对象是一个从原始队列中“过滤后”的队列 


filter   
[expr for iter_var in iterable if condition_expr]

def odd(n):return n%2

seq=[11,10,9,9,10,10,9,8,7,6,5,4,3,2,1]
filter(lambda x:x%2,seq)                     ###[11, 9, 9, 9, 7, 5, 3, 1]

[x for x in seq if x%2]                      ###[11, 9, 9, 9, 7, 5, 3, 1]


def filter(bool_func,seq):
  filter_seq=[]
  for eachItem in seq:
    if bool_func(eachItem):
      filter_seq.append(eachItem)
  return filter_seq

就想上面的方法,经一个序列根据一定的条件进行过滤,最后返回一个新的序列.


method 1  

from random import randint
def odd(n):
    return n % 2

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))

print filter(odd, allNums)


method 2
from random import randint
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))

print filter(lambda n: n%2, allNums)


method 3
from random import randint
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))

print [n for n in allNums if n%2]


method 4
from random import randint 
print [n for n in [randint(1,99) for i in range(9)] if n%2]

