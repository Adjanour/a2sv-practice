import sys

n = int(sys.stdin.readline().strip())

phone_book = {}

for _ in range(n):
    name, number = sys.stdin.readline().split()
    phone_book[name] = number

for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
