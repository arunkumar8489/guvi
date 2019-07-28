def nu(n): 
      n= n.lower()
      n= set(n)
      a = [ ch for ch in n if ord(ch) in range(ord('a'), ord('z')+1)]
      if len(a) == 26: 
        return 'yes'
      else: 
        return 'no'
n=input()
print(nu(n)) 
