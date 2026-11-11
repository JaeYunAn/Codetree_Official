def make_a():
    n, m = map(int, input().split())

    number_list = []
    number_list.append(n)
    number_list.append(m)

    i_list = []
    for i in range(1, min(number_list) + 1):
        if n % i == 0 and m % i == 0:
            i_list.append(i)

    print(max(i_list))

make_a()