def f():
    n = int(input())
    n_list = [list(input()) for _ in range(n)]
    n_list.sort()

    for i in n_list:
        print(''.join(i))

f()