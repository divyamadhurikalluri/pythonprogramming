N=int(raw_input())
p=[]
x=0
for i in range(N):
  p.append(raw_input().split())
for j in range(N):
  x=x+int(p[i][j])
print x  
