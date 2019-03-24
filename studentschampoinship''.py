N,k=map(eval,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
s=0
for i in a:
  if i<=(5-k):
    s+=1
'''
c=0
while c<len(a):
  if a[c]+k<=5:
    s+=1
  c+=1
'''  
print(s//3)
