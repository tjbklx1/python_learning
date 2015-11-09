reduce内建函数是一个二元操作函数，
他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给reduce中的函数 func()（必须是一个二元操作函数） 先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
如：
def myadd(x,y):  
    return x+y
   
sum=reduce(myadd,(1,2,3,4,5,6,7))  
print sum  

#结果就是输出1+2+3+4+5+6+7的结果即28
当然，也可以用lambda的方法，更为简单：

sum=reduce(lambda x,y:x+y,(1,2,3,4,5,6,7))  
print sum  

总结:

def myadd(x,y): return x+y
sum=reduce(myadd,(1,2,3,4,5,6,7))  
print sum                                     ###28
sum=reduce(lambda x,y:x+y,(1,2,3,4,5,6,7))  
print sum                                     ###28


reduce
使用了一个二元函数（一个接收带带两个值作为输入，进行了一些计算然后返回一个值作为输出）,一个序列，和一个可选的初始化器，卓有成效地将那个列表的内容“减少”为一个单一的值

它通过取出序列的头两个元素，将他们传入二元函数来获得一个单一的值来实现。
然后又用这个值和序列的下一个元素来获得又一个值，然后继续直到整个序列的内容都遍历完毕以及最后的值会被计算出来为止。
你可以尝试去形象化reduce 如下面的等同的例子：
reduce(func, [1, 2, 3]) = func(func(1, 2), 3)


n=5
print ( reduce(lambda x,y:x*y,range(1,n+1)) )    ###120

分布演示:

def mySum(x,y): return x+y
allNums = range(5)                ### [0, 1, 2, 3, 4]
total = 0
for eachNum in allNums:
    total = mySum(total, eachNum)

print 'the total is:', total      ###the total is: 10

使用lambda 和reduce(),我们可以以一行代码做出相同的事情。

print 'the total is:', reduce((lambda x,y: x+y), range(5))   ###the total is: 10

解释:
给出了上面的输入，reduce（）函数运行了如下的算术操作。 
((((0 + 1) + 2) + 3) + 4) = 10

用list 的头两个元素（0，1），调用mySum()来得到1,然后用现在的结果和下一个元素2 来再次调用mySum()， 再从这次调用中获得结果，与下面的元素3 配对然后调用mySum()，最终拿整个前面的求和和4 来调用mySum()得到10，10 即为最终的返回值。 



总结:
def mySum(x,y): return x+y
reduce(mySum, [1, 2, 3])    ###6
print 'the total is:', reduce((lambda x,y: x+y), range(5))   ###the total is: 10

reduce 有点像for循环 只是更开始拿到头两个元素,计算后,再和第三个元素计算

