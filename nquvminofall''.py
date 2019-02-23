N,Q=map(int,(raw_input()).split())
x=list(map(int,(raw_input()).split()))
a=[]
for i in range(0,Q):
    U,V=map(int,(raw_input()).split())
    s=0
    m=x[U-1]
    for j in range(U-1,V):
      if (x[j]<m):
        m=x[j]
    a.append(m)
print(a[0])
print(a[1])
print(a[2])
