def deco(arg):
    def _deco(func):
        def __deco():
            print("---- before %s called [%s].  ----" % (func.__name__,arg))
            func()
            print("---- after  %s called [%s].  ----" % (func.__name__,arg))
        return __deco
    return _deco
 
@deco("mymodule")
def myfunc():
    print(" myfunc() called.")
 
@deco("module2")
def myfunc2():
    print(" myfunc2() called.")
 
myfunc()
print ""
myfunc2()

#---- before myfunc called [mymodule].  ----
# myfunc() called.
#---- after  myfunc called [mymodule].  ----
#
#---- before myfunc2 called [module2].  ----
# myfunc2() called.
#---- after  myfunc2 called [module2].  ----


