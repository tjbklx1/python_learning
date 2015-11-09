def deco(func):
    def _deco(a,b):
        print("---- before myfunc() called. ----")
        ret=func(a,b)
        print("---- after myfunc() called. result: %s   ----" % ret)
        return ret
    return _deco
 
@deco
def myfunc(a,b):
    print("     myfunc(%s,%s) called." %(a,b))
    return a+b
 
myfunc(1,2)
print "**********************************"
myfunc(3,4)

#---- before myfunc() called. ----
#     myfunc(1,2) called.
#---- after myfunc() called. result: 3   ----
#**********************************
#---- before myfunc() called. ----
#     myfunc(3,4) called.
#---- after myfunc() called. result: 7   ----