S=raw_input()
x=[]
for i in S:
  if(i not in x):
    x.append(i)
if((len(x)==27) or (len(x)==28)):
  print("yes")
else:
  print("no")  
    
