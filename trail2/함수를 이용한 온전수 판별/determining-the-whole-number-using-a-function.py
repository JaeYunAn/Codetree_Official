def f():
    A, B = map(int, input().split())
    count = 0
    for i in range(A, B + 1):
        if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
            continue
        else:
            count += 1

    return count
print(f())