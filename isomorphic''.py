s1,s2=raw_input().split()
n=0
for x in range(0,len(s1)):
  if((ord(s1[x])-ord(s1[x-1]))!=(ord(s2[x])-ord(s2[x-1]))):
    n+=1
if(n>0):
  print("no")
else:
  print("yes")
'''
s1,s2=raw_input().split()
n=0
for x in range(0,len(s1)):
  if((ord(s1[x])-ord(s1[x-1]))==(ord(s2[x])-ord(s2[x-1]))):
    print("yes")
    break
else:
  print("no")
 '''
