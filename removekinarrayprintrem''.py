N,K=map(int,input().split())
a=list(map(int,input().split()))
p=[]
for x in range(0,len(a)):
  if(a[x]!=K):
    p.append(a[x])
if(len(p)>0):
  print(" ".join(map(str,p)))
else:
  print("empty")
