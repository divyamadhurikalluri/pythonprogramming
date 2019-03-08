N,M=map(int,raw_input().split())
if N<=M:
  a=N
else:
  a=M
b=[]
for x in range(0,a):
  b.append(sorted(list(map(int,raw_input().split()))))
b=sorted(b)
for x in range(0,len(b[0])):
  for y in range(0,len(b)-1):
    if b[y][x]>b[y+1][x]:
      b[y][x],b[y+1][x]=b[y+1][x],b[y][x]
for x in b:
  print(' '.join(map(str,x)))
