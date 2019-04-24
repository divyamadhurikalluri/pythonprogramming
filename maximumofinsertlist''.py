n,m=map(int,input().split())
v=input()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=0
for i in range(0,len(b)):
  a.append(b[i])
  if p==0:
    print(max(a),end="")
    p+=1
  else:
    print("",max(a),end="")
