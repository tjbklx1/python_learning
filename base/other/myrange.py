def myreverse(data):
    for index in range(0,len(data),1):
        yield data[index]
       
for char in myreverse("reboot"):
    print char,
    
print ""
   
for char in range(10):
    print char,    
 
print ""

for char in range(10,20,2):
    print char,    
    
    
    
    