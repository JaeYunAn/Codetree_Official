N_1, N_2 = map(int, input().split())
A = ' ' + ' '.join(input().split()) + ' '
B = ' ' + ' '.join(input().split()) + ' '

if B in A:
    print('Yes')
else:
    print('No')