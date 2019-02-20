a,b=map(int,raw_input().split())
p,q=map(int,raw_input().split())
x,y=map(int,raw_input().split())
if((a==p==x) or (b==q==y)):
  print("yes")
elif(((q-b)/(p-a))==((y-b)/(x-a))):
  print("yes")
else:
  print("no")    

