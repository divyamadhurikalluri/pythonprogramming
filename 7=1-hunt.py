N=int(input())
B=raw_input().split()
A=[]
if N==len(B):
  for i in range(0,len(B)):
    if i%2==0:
      B[i]=int(B[i])
      if ((B[i]%2)!=0):
        A.append(B[i])
    else:
      B[i]=int(B[i])
      if B[i]%2==0:
        A.append(B[i])
print (' '.join(map(str,A)))        
 
