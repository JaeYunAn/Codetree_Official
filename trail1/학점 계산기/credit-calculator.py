N = int(input())
numbers = list(map(float, input().split()))

numbers_avg = sum(numbers) / len(numbers)

if numbers_avg >= 4.0:
    print(f'{numbers_avg:.1f}')
    print('Perfect')
elif numbers_avg >= 3.0:
    print(f'{numbers_avg:.1f}')
    print('Good')
else:
    print(f'{numbers_avg:.1f}')
    print('Poor')