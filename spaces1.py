N=raw_input()
N=N.split(' ')
while '' in N:
    N.remove('')
N=' '.join(N)
print(N)
