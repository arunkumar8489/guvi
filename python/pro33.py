def nu(n):
    for i in range(len(n)):
      if(n[i] < n[i+1]):
        print(n[i+1:])
        break
n=input()
nu(n)
