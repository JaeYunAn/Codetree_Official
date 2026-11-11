def f():
    A, B = map(int, input().split())
    count = 0
    for i in range(A, B + 1):
        if i % 3 == 0 or '3' in str(i) or '6' in str(i) or '9' in str(i):
            count += 1
    return count

print(f())