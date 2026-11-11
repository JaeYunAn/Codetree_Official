def is_prime(n):
    if n < 2:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

def digit_sum_even(n):
    total = 0
    for ch in str(n):
        total += int(ch)
    return total % 2 == 0

def f():
    A, B = map(int, input().split())
    count = 0
    for i in range(A, B + 1):
        if is_prime(i) and digit_sum_even(i):
            count += 1
    return count

print(f())