S=str(raw_input())
a=[]
b=['d','h','o','n','i']
b.sort()
for i in S:
  a.append(i)
a.sort()
if(b==a):
  print("yes")
else:
  print("no")
