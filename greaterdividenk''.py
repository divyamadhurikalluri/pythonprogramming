N,K=map(int,raw_input().split())
x=0
y=K-1
while(x==0 and y>1):
  if(N%y==0 and K%y==0):
    x+=1
  y-=1  
print (y+1)    
