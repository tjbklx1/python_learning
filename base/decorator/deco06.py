def deco(func):
    def _deco(*args,**kwargs):
        print("---- before %s called. ----" % (func.__name__))
        ret=func(*args,**kwargs)
        print("---- after %s called. result: %s   ----" % (func.__name__,ret))
        return ret
    return _deco
 
@deco
def myfunc(a,b):
    print("     myfunc(%s,%s) called." %(a,b))
    return a+b
    
@deco
def myfunc2(a,b,c):
    print("     myfunc2(%s,%s,%s) called." %(a,b,c))
    return a+b+c
 
myfunc(1,2)
print "**********************************"
myfunc(3,4)
print "**********************************"
myfunc2(3,4,5)
print "**********************************"
myfunc2(3,4,10)


#---- before myfunc called. ----
#     myfunc(1,2) called.
#---- after myfunc called. result: 3   ----
#**********************************
#---- before myfunc called. ----
#     myfunc(3,4) called.
#---- after myfunc called. result: 7   ----
#**********************************
#---- before myfunc2 called. ----
#     myfunc2(3,4,5) called.
#---- after myfunc2 called. result: 12   ----
#**********************************
#---- before myfunc2 called. ----
#     myfunc2(3,4,10) called.
#---- after myfunc2 called. result: 17   ----