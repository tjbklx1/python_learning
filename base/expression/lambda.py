lambda     允许你快速的创建只有一行的函数对象
map()      对所有成员应用一个操作
filter()   基于一个条件表达式过滤成员列表
reduce()


内建函数apply()、filter()、map()、reduce()

apply(func[, nkw][, kw]) 用可选的参数来调用func，nkw 为非关键字参数，kw 关键字参数；返回值是函数调用的返回值。

filter(func, seq)b 调用一个布尔函数func 来迭代遍历每个seq 中的元素； 返回一个使func 返回值为ture 的元素的序列。

map(func, seq1[,seq2...])b 将函数func 作用于给定序列（s)的每个元素，并用一个列表来提供返回值；
如果func 为None， func 表现为一个身份函数，返回一个含有每个序列中元素集合的n 个元组的列表。

reduce(func, seq[, init])
将二元函数作用于seq 序列的元素， 每次携带一对（先前的结果以及下一个序列元素），连续的将现有的结果和下雨给值作用在获得的随后的结果上，最后减少我们的序列为一个单一的返回值；
如果初始值init 给定，第一个比较会是init 和第一个序列元素而不是序列的头两个元素。

apply 可以有效的取代1.6，在其后的python 版本中逐渐淘汰。
b.由于在python2.0 中，列表的综合使用的引入，部分被摈弃。


f=lambda x,y,z:x+y+z
print ( f(1,2,3) )

def action(x):
   return lambda y:x+y
   
a=action(2)
print a(22)
print a(33)

b=lambda x:lambda y:x+y
a=b(3)
print a(2)
print (b(3))(2)
print (b(3))(10)
print (b(30))(10)

#6
#24
#35
#5
#5
#13
#40

[expr for iter_var in iterable]

>>> a=lambda x:x**2
>>> a(10)
100

map( lambda x:x**2,range(6) )
>>> map( lambda x:x**2,range(6) )
[0, 1, 4, 9, 16, 25]

相当于[(x**2) for x in range(6)]
>>> [(x**2) for x in range(6)]
[0, 1, 4, 9, 16, 25]





lambda 
核心笔记：lambda 表达式返回可调用的函数对象。
用合适的表达式调用一个lambda 生成一个可以像其他函数一样使用的函数对象。
它们可被传入给其他函数，用额外的引用别名化，作为容器对象以及作为可调用的对象被调用（如果需要的话，可以带参数）。
当被调用的时候，如过给定相同的参数的话，这些对象会生成一个和相同表达式等价的结果。
它们和那些返回等价表达式计算值相同的函数是不能区分的。

def true():return True

lambda :True
true=lambda :True
true()

def add(x, y): return x + y
lambda x, y: x + y

>>> a=lambda x,y=2:x+y
>>> a(3)
5
>>> a(3,5)
8
>>> a(0)
2
>>> a(0,9)
9


>>> b=lambda *z:z
>>> b(23,'xyz')
(23, 'xyz')
>>> b(42)
(42,)







更多案例:
1,迭代一个3行5列的矩阵
[  (x+1,y+1) for x in range(3) for y in range(5)  ]

>>> [  (x+1,y+1) for x in range(3) for y in range(5)  ]
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]

>>> [  (x,y) for x in range(3) for y in range(5)  ]
[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]


2,计算所有非空白字符的数目
vi 500.txt
When it comes to the creation of world-changing ideas, startups get all the acclaim. We get it—being the new kid on the block is a blessing, not a curse, in the land of innovation. But that's not the whole picture. A number of landmark tools and technologies can be credited to clever people working for some of the largest companies on the planet. Xerox (No. 143) XRX0.38%in the 1970s invented Ethernet, now a fixture of the modern Internet-connected office. Motorola (No. 363) MSI0.45%in the 1980s developed Six Sigma, a set of process-improvement techniques that changed the way Fortune 500 companies operated. And Walmart's (No. 1) WMT1.34%use of "continuous replenishment" for inventory in the 1990s is a key reason it has spent more than a decade at or near the top of our iconic list. What will the next 10 years bring? Hard to say—but these five movers and shakers are among those best positioned to grasp it. Read on to discover Fortune's 2015 Accelerators. 

>>> f=open('500.txt','r')
>>> len([word for line in f for word in line.split()])
164
>>> import os
>>> os.stat('500.txt').st_size
967
>>> f.seek(0)
>>> sum([len(word) for line in f for word in line.split()])
803
