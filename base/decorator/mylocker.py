class mylocker:
    def __init__(self):
        print(">>>>mylocker.__init__() called.")
         
    @staticmethod
    def acquire():
        print("----mylocker.acquire() called.")
         
    @staticmethod
    def unlock():
        print("----mylocker.unlock() called.")
 
class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("====lockerex.acquire() called.")
         
    @staticmethod
    def unlock():
        print("====lockerex.unlock() called.")
 
def lockhelper(cls):
    '''cls must have the staticmethod acquire and release.'''
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco
    