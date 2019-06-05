jk = float(input("Enter first number: "))
kl = float(input("Enter second number: "))
lp = float(input("Enter third number: "))
 
if (jk > kl) and (jk > lp):
   largest = jk
elif (kl > lp) and (kl > lp):
   largest = kl
else:
   largest = lp
 
print("The largest number is",largest)
