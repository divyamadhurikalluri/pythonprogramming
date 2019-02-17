S=raw_input()
print(''.join([j for i,j in enumerate(S) if j not in S[:i]]))
