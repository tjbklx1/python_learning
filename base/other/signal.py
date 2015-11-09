import signal,functools

class TimeoutError(Exception):
    pass
    
    
def timeout(seconds,error_message='Function call time out'):
    def decorated(func):
    
        def _handle_timeout(signum,frame):
            raise TimeoutError(error_message)
        
        def wrapper(*args,**kwargs):
            signal.signal(signal.SIGALRM,_handle_timeout)
            signal.alarm(seconds)
            try:
                result=func(*args,**kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)
    return decorated
    
    
@timeout(5)
def slowfunc(sleep_time):
    import time
    time.sleep(sleep_time)
    
slowfunc(3)
print "-----------------------------------------------"
slowfunc(10)


#[oracle@DBA-TEST tmp]$ python test_signal.py 
#-----------------------------------------------
#Traceback (most recent call last):
#  File "test_signal.py", line 33, in <module>
#    slowfunc(10)
#  File "test_signal.py", line 17, in wrapper
#    result=func(*args,**kwargs)
#  File "test_signal.py", line 29, in slowfunc
#    time.sleep(sleep_time)
#  File "test_signal.py", line 11, in _handle_timeout
#    raise TimeoutError(error_message)
#__main__.TimeoutError: Function call time out