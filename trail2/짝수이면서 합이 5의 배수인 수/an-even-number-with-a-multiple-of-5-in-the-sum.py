def f():
    n = input()
    n_sum = 0
    for i in range(len(n)):
        n_sum += int(n[i])

    if int(n) % 2 == 0 and n_sum % 5 == 0:
        print('Yes')
    else:
        print('No')
f()