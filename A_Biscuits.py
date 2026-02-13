import sys

iterator = iter(sys.stdin.read().strip().split())
t = int(next(iterator))
out = []

for _ in range(t): #number of test cases
    n = int(next(iterator))
    out.append(str((n-1) // 2))

print("\n".join(out))