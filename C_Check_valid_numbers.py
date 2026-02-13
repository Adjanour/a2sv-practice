import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it)); m = int(next(it)); p = int(next(it)); q = int(next(it))
    if n % p != 0:
        out.append("YES")
    else:
        out.append("YES" if m == (n // p) * q else "NO")
print("\n".join(out))
