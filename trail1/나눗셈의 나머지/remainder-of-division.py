A, B = map(int, input().split())

num_list = []

while A > 1:
    num_list.append(A % B)
    A //= B

num_list_new = [0] * B

for i in num_list:
    num_list_new[i] += 1

num_list_new_sum = 0

for j in num_list_new:
    num_list_new_sum += j ** 2
print(num_list_new_sum)