p1, p1t1 = input().split()
p2, p2t1 = input().split()
p3, p3t1 = input().split()

p1t = int(p1t1)
p2t = int(p2t1)
p3t = int(p3t1)

p = []
pt = []

p.append(p1)
p.append(p2)
p.append(p3)

pt.append(p1t)
pt.append(p2t)
pt.append(p3t)

hospital = [0] * 4

for i in range(3):
    if p[i] == 'Y' and pt[i] >= 37:
        hospital[0] += 1

    elif p[i] == 'N' and pt[i] >= 37:
        hospital[1] += 1

    elif p[i] == 'Y' and pt[i] < 37:
        hospital[2] += 1

    elif p[i] == 'N' and pt[i] < 37:
        hospital[3] += 1

if hospital[0] >= 2:
    print(*hospital, 'E')
else:
    print(*hospital)