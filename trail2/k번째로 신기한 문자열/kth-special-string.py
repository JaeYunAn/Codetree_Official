def f():
    N, K, T = input().split()
    N = int(N)
    K = int(K)
    text = [input() for _ in range(N)]
    text_new = []

    for i in text:
        text_ap = i[:len(T)]
        if T == text_ap:
            text_new.append(i)
    text_new.sort()
    print(text_new[K - 1])

f()