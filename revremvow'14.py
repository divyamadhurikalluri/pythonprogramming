
N=int(raw_input())
S=raw_input()
x=S[::-1]
for i in "aeiouAEIOU":
  x=x.replace(i,"")
print x  
