filter
����һ����������к�һ�������ˡ�������ÿ������Ԫ�ض�ͨ���������������ɸѡ�� ������������Ϊ��ĵĶ���
filter ����Ϊ��֪�����е�ÿ��Ԫ�ص��ø�������������ÿ��filter ���صķ��㣨true)ֵԪ����ӵ�һ���б��С� ���صĶ�����һ����ԭʼ�����С����˺󡱵Ķ��� 


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

��������ķ���,��һ�����и���һ�����������й���,��󷵻�һ���µ�����.


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

