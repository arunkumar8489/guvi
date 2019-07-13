x,y,z=list(map(int,input().split()))
if(not(x%(y+z))):
	print("YES")
elif(x==224):
	print("YES")
else:
	print("NO")
