N=input()
M=input()
for i in range(N,M+1):
    if(i>1):
       for K in range(2,i):
           if(i%K==0):
               break
       else:
           print(i)
             
