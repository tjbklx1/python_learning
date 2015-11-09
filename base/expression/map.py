map()
将函数调用“映射”到每个序列的元素上，并返回一个含有所有返回值的列表。
map()带一个函数和队列， 将函数作用在序列的每个元素上， 然后创建由每次函数应用组成的返回值列表。

def mymap(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq

mymap((lambda x: x+2), [0, 1, 2, 3, 4, 5])      ###[2, 3, 4, 5, 6, 7]

mymap(lambda x: x**2, range(6))                 ###[0, 1, 4, 9, 16, 25]

[x+2 for x in range(6)]                         ###[2, 3, 4, 5, 6, 7]

[x**2 for x in range(6)]                         ###[0, 1, 4, 9, 16, 25]


map 多个序列

map(lambda x, y: x + y, [1,3,5], [2,4,6])       ###[3, 7, 11]

map(lambda x, y: (x+y, x-y), [1,3,5], [2,4,6])  ###[(3, -1), (7, -1), (11, -1)]

map(None, [1,3,5], [2,4,6])                     ###[(1, 2), (3, 4), (5, 6)]

zip( [1,3,5], [2,4,6])                          ###[(1, 2), (3, 4), (5, 6)]