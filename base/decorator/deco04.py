def deco(func):
    def _deco():
        print("---- before myfunc() called. ----")
        func()
        print("---- after myfunc() called.  ----")
    return _deco
 
@deco
def myfunc():
    print("     myfunc() called.")
    return 'ok'
 
myfunc()
print "**********************************"
myfunc()

#---- before myfunc() called. ----
#     myfunc() called.
#---- after myfunc() called.  ----
#**********************************
#---- before myfunc() called. ----
#     myfunc() called.
#---- after myfunc() called.  ----