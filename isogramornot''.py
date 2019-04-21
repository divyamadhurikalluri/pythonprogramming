S=raw_input()
a=[]
for i in S:
  a.append(i)
b=set(a)
if len(a)==len(b):
  print("Yes")
else:
  print("No") 
