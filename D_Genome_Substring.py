def get_dist(c1, c2):
    v1 = ord(c1) - ord('A')
    v2 = ord(c2) - ord('A')
    diff = abs(v1 - v2)
    return min(diff, 26 - diff)

def solve():
    n = int(input())
    s = input()
    target = "ACTG"
    min_ops = float('inf')
    
    # Check every possible start position for "ACTG"
    for i in range(n - 3):
        current_ops = 0
        for j in range(4):
            current_ops += get_dist(s[i + j], target[j])
        min_ops = min(min_ops, current_ops)
        
    print(min_ops)


solve()