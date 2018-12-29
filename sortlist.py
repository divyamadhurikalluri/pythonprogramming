N=int(input())
a=[]
for v in range(N):
    i=input()
    a.append(i)   
if sorted(a)==a:
   print('yes')
else:
   print('no')    
