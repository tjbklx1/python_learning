def fob(max):
    n,a,b=0,0,1
    while n<max:
        print b,
        a,b=b,a+b 
        n=n+1
        
fob(5)

#1 1 2 3 5

print "\n-------------------------------"

def fob2(max):
    n,a,b=0,0,1
    L=[]
    while n<max:
        L.append(b)
        a,b=b,a+b 
        n=n+1
    return L
        
for n in fob2(5):
    print n,
    
print "\n-------------------------------"


def fob3(max):
    n,a,b=0,0,1
    while n<max:
        yield b,
        a,b=b,a+b 
        n=n+1
        
for n in fob3(5):
    print n,


