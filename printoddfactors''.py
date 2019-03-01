N=int(raw_input())
a=[]
for x in range(1,N+1):
    if(N%x==0 and x%2!=0):
        a.append(x)
print(" ".join(map(str,a)))


'''

n=int(input())
for i in range(1,n+1):
    if(i%2!=0 and n%i==0):
        print(i,end=' ')
        
'''
