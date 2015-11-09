class locker:
    def __init__(self):
        print(">>>>locker.__init__() should be not called.")
         
    @staticmethod
    def acquire():
        print(">>>>locker.acquire() called. (staticmethod)")
         
    @staticmethod
    def release():
        print(">>>>locker.release() called. (did not instance)")
 
def deco(cls):
    '''cls must have the staticmethod acquire and release.'''
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco
 
@deco(locker)
def myfunc():
    print("    myfunc() called.")
 
myfunc()
print ""
myfunc()



#before myfunc called [__main__.locker].
#>>>>locker.acquire() called. (staticmethod)
#    myfunc() called.
#>>>>locker.release() called. (did not instance)
#
#before myfunc called [__main__.locker].
#>>>>locker.acquire() called. (staticmethod)
#    myfunc() called.
#>>>>locker.release() called. (did not instance)

