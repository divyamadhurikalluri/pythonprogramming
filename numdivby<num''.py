N=int(raw_input())
c=0
for x in range(2,N):
    if(N%x==0):
        c=c+1
if(c!=0):
    print("yes")
else:
    print("no")

'''

N=int(raw_input())
for x in range(2,N):
  if(N%x==0):
    print("yes")
    break
  else:
    print("no")    
    break


'''

    
