class myxrange:
    def __init__(self,lower=0,upper=0,step=1):
        if lower <upper:
            self.lower=lower
            self.upper=upper
        else :
            self.lower=upper
            self.upper=lower
        self.step=step
    
    def __iter__(self):
        #print  ( "%d ,%d ,%d \n") %(self.lower,self.upper,self.step)
        lower=self.lower
        upper=self.upper 
        if self.step>0:            
            while lower<self.upper :
                yield lower
                lower+=self.step 
                
        else:
            while upper>self.lower :
                yield upper 
                upper+=self.step 
                

      
for i in myxrange(5):
    print i,
  
print ""

for i in myxrange(0,10):
    print i,

print ""
    
for i in myxrange(10,20,2):
    print i,

print ""
    
for i in myxrange(40,20,-3):
    print i,

print ""

for i in myxrange(lower=0,upper=10,step=3):
    print i,

print ""
    
for i in myxrange(lower=100,upper=80,step=-2):
    print i,
    
print ""   


