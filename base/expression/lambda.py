lambda     ��������ٵĴ���ֻ��һ�еĺ�������
map()      �����г�ԱӦ��һ������
filter()   ����һ���������ʽ���˳�Ա�б�
reduce()


�ڽ�����apply()��filter()��map()��reduce()

apply(func[, nkw][, kw]) �ÿ�ѡ�Ĳ���������func��nkw Ϊ�ǹؼ��ֲ�����kw �ؼ��ֲ���������ֵ�Ǻ������õķ���ֵ��

filter(func, seq)b ����һ����������func ����������ÿ��seq �е�Ԫ�أ� ����һ��ʹfunc ����ֵΪture ��Ԫ�ص����С�

map(func, seq1[,seq2...])b ������func �����ڸ������У�s)��ÿ��Ԫ�أ�����һ���б����ṩ����ֵ��
���func ΪNone�� func ����Ϊһ����ݺ���������һ������ÿ��������Ԫ�ؼ��ϵ�n ��Ԫ����б�

reduce(func, seq[, init])
����Ԫ����������seq ���е�Ԫ�أ� ÿ��Я��һ�ԣ���ǰ�Ľ���Լ���һ������Ԫ�أ��������Ľ����еĽ���������ֵ�����ڻ�õ����Ľ���ϣ����������ǵ�����Ϊһ����һ�ķ���ֵ��
�����ʼֵinit ��������һ���Ƚϻ���init �͵�һ������Ԫ�ض��������е�ͷ����Ԫ�ء�

apply ������Ч��ȡ��1.6��������python �汾������̭��
b.������python2.0 �У��б���ۺ�ʹ�õ����룬���ֱ�������


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

�൱��[(x**2) for x in range(6)]
>>> [(x**2) for x in range(6)]
[0, 1, 4, 9, 16, 25]





lambda 
���ıʼǣ�lambda ���ʽ���ؿɵ��õĺ�������
�ú��ʵı��ʽ����һ��lambda ����һ����������������һ��ʹ�õĺ�������
���ǿɱ�����������������ö�������ñ���������Ϊ���������Լ���Ϊ�ɵ��õĶ��󱻵��ã������Ҫ�Ļ������Դ���������
�������õ�ʱ�����������ͬ�Ĳ����Ļ�����Щ���������һ������ͬ���ʽ�ȼ۵Ľ����
���Ǻ���Щ���صȼ۱��ʽ����ֵ��ͬ�ĺ����ǲ������ֵġ�

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







���స��:
1,����һ��3��5�еľ���
[  (x+1,y+1) for x in range(3) for y in range(5)  ]

>>> [  (x+1,y+1) for x in range(3) for y in range(5)  ]
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]

>>> [  (x,y) for x in range(3) for y in range(5)  ]
[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]


2,�������зǿհ��ַ�����Ŀ
vi 500.txt
When it comes to the creation of world-changing ideas, startups get all the acclaim. We get it��being the new kid on the block is a blessing, not a curse, in the land of innovation. But that's not the whole picture. A number of landmark tools and technologies can be credited to clever people working for some of the largest companies on the planet. Xerox (No. 143) XRX0.38%in the 1970s invented Ethernet, now a fixture of the modern Internet-connected office. Motorola (No. 363) MSI0.45%in the 1980s developed Six Sigma, a set of process-improvement techniques that changed the way Fortune 500 companies operated. And Walmart's (No. 1) WMT1.34%use of "continuous replenishment" for inventory in the 1990s is a key reason it has spent more than a decade at or near the top of our iconic list. What will the next 10 years bring? Hard to say��but these five movers and shakers are among those best positioned to grasp it. Read on to discover Fortune's 2015 Accelerators. 

>>> f=open('500.txt','r')
>>> len([word for line in f for word in line.split()])
164
>>> import os
>>> os.stat('500.txt').st_size
967
>>> f.seek(0)
>>> sum([len(word) for line in f for word in line.split()])
803
