n=raw_input() 
l=map(int,raw_input().split())
a=[]
for i in range(0,len(l)):
  if(int(l[i])==i):
    a.append(i)
if(len(a)!=0):
  print(' '.join(map(str,a))) 
else:
  print('-1')    
