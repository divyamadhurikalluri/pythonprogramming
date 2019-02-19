N,M=map(int,raw_input().split())
if(M>N):
  p=M
else:
  p=N
while(True):
  if(p%M==0 and p%N==0):
    x=p
    break
  p+=1
print x 
