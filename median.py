N,m=int(input()),[]
for i in range(1,N+1):
    a=int(input())
    m.append(a)
m.sort()
print(m)
if N%2==1:
    n=m[i//2]    
    print(n)
else:
    n=((m[i//2]+m[i//2-1])/2)    
    print(n)

