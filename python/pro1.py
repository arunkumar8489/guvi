def l(str1,str2):
        if(str1 in str2):
            return str1
        else:
            return l(str1[0:len(str1)-1],str2)
m = int(input())
x= []
for _ in range(0,m):
    x.append(input())
x.sort()
print(l(x[0],x[m-1]))
