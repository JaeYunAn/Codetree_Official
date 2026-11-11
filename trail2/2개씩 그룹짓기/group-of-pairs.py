def f():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    nums_1 = nums[::-1]
    nums_2 = []
    nums_3 = []
    nums_4 = []

    for i in range(N):
        nums_2.append(nums[i])
        nums_3.append(nums_1[i])

    for j in range(N):
        nums_4.append(nums_2[j] + nums_3[j])

    print(max(nums_4))
f()