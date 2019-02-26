S=str(raw_input())
a=0
for i in range(0,len(S)):
  if(S[i]=='('):
    a+=1
  if(S[i]==')'):
    a-=1
if(a==0):
  print("yes")
else:
  print("no")
