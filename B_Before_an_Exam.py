d, sumTime = map(int, input().split())

mins = []
maxs = []

for _ in range(d):
    a, b = map(int, input().split())
    mins.append(a)
    maxs.append(b)

minSum = sum(mins)
maxSum = sum(maxs)

# Check feasibility
if sumTime < minSum or sumTime > maxSum:
    print("NO")
else:
    print("YES")
    schedule = mins[:]  # start with minimums
    remaining = sumTime - minSum

    for i in range(d):
        if remaining == 0:
            break
        can_add = maxs[i] - mins[i]
        add = min(can_add, remaining)
        schedule[i] += add
        remaining -= add

    print(*schedule)
