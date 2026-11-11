scores = list(map(int, input().split()))

scores_new = []
scores_new_new = []

for i in scores:
    if i == 0:
        break
    elif i >= 10:
        scores_new.append(i)

for j in scores_new:
    scores_new_new.append(j // 10)

scores_new_new_new = [0] * 10

for k in scores_new_new:
    scores_new_new_new[k - 1] += 1

for L in range(9, -1, -1):
    print(f'{(L + 1) * 10} - {scores_new_new_new[L]}')