N=int(raw_input())
a=list(map(int,raw_input().split()))
b=[]
c=1
for i in a:
  if i not in b:
    b.append(i)
for i in range(0,len(b)-1):
  if b[i]<b[i+1]:
    c+=1
print(c)
