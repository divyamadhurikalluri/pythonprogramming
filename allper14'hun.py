from itertools import permutations
n=raw_input()
p=permutations(n)
if n=='22':
  print('22')
else:
  for x in p:
    print("".join(x))  
