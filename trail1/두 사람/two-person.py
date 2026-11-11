age_A, gender_A = input().split()
age_B, gender_B = input().split()
age_A = int(age_A)
age_B = int(age_B)

if (age_A >= 19 and gender_A == 'M') or (age_B >= 19 and gender_B == 'M'):
    print(1)
else:
    print(0)