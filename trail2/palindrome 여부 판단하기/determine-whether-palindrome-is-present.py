def f():
    A = input()
    if A[::-1] == A:
        return 'Yes'
    else:
        return 'No'
print(f())