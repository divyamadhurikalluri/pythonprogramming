N,A,B=map(int,raw_input().split())
d=A*4+B*4
if(N==2 and A==1 and B==1):
    print("YES")
elif(N==d):
    print("YES")
else:
    print("NO")
