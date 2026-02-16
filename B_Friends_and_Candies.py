import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        s = sum(a)
        if s % n != 0:
            out.append("-1")
            continue
        x = s // n
        out.append(str(sum(1 for v in a if v != x)))
print("\n".join(out))
