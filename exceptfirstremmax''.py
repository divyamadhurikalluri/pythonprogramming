N= int(input())
a= list(map(int,input().split()))
p=[]
for x in range(N-1):
    y= max(a[x+1:])
    p.append(str(y))
p.append(str(0))
print(" ".join(map(str,p)))
