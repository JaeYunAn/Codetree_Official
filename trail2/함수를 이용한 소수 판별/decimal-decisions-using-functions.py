def f():
    A, B = map(int, input().split())
    num_list = []

    for i in range(A, B + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num_list.append(i)

    return sum(num_list)

print(f())