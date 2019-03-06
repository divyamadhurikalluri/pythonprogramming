k=int(raw_input())
a,b=[],[]
for x in range(0,k):
  a=sorted(list(map(int,raw_input().split())))
  b=b+a
c=sorted(b)
print(' '.join(map(str,c)))
