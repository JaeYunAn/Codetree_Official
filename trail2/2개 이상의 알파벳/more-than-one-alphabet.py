def f():
    A = list(input())
    count = 0
    for i in A:
        for j in A:
            if j != i:
                count += 1
    if count >= 2:
        return 'Yes'
    else:
        return 'No'
print(f())