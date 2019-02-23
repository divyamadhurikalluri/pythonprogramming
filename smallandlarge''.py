N=int(raw_input())
a=raw_input().split()
b=[]
x=[]
for i in a:
    b.append(int(i))
c=(b.index(min(b))+1)
d=(b.index(max(b))+1)
x.append(c)
x.append(d)
print(' '.join(map(str,x)))
