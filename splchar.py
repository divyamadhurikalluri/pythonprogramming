s,k,l,m=raw_input(),0,0,0
for i in s:
   if i.isdigit():
       k+=1
   elif i.isalpha():
       l+=1
   else:
       m+=1   
print(m)   
