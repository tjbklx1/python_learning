import sys
import os
import linecache

def trace(f):
    def globaltrace(frame,why,arg):
        if why=='call':
            return localtrace
        return None
    
    def localtrace(frame,why,arg):
        if why=='line':
            # record the line file name and line number of every trace
            filename=frame.f_code.co_filename
            lineno=frame.f_lineno
            bname=os.path.basename(filename)
            print "{}({}):{}".format(bname,lineno,linecache.getline(filename,lineno)),
        return localtrace
    
    def _f(*args,**kwargs):
        sys.settrace(globaltrace)
        result=f(*args,**kwargs)
        sys.settrace(None)
        return result

    return _f
    
@trace
def testfunction():
    print 1
    print 22
    print 333
    
    
testfunction()


#>python test_trace.py
#test_trace.py(30):    print 1
#1
#test_trace.py(31):    print 22
#22
#test_trace.py(32):    print 333
#333