def f():
    a, o, c = input().split()

    a = int(a)
    c = int(c)

    if o not in '+-*/':
        return False

    if o == '+':
        return f'{a} {o} {c} = {a + c}'
    elif o == '-':
        return f'{a} {o} {c} = {a - c}'
    elif o == '*':
        return f'{a} {o} {c} = {a * c}'
    elif o == '/':
        return f'{a} {o} {c} = {a // c}'

print(f())