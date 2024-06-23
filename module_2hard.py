import random
ran = int(random.uniform(3, 20))
spis = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
ans = []
for i in spis:
    for j in spis:
        if i == j:
            continue
        if ran % (i + j) == 0:
            ans.append(i)
            ans.append(j)
            continue

print(*ans)

