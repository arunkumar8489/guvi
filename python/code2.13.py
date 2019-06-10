nu = int(input())
  
if nu > 1: 
        
   for i in range(2, nu//2): 
       if (nu % i) == 0: 
           print("no") 
           break
   else: 
       print("yes") 
  
else: 
   print("no") 
