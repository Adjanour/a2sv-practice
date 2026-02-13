import sys

input_data = sys.stdin.read().split()

t = int(input_data[0])
results = []
    
for i in range(1, t + 1):
    n = int(input_data[i])
        
    if n == 2:
        results.append("2")
    elif n == 3:
        results.append("3")
    elif n % 2 == 0:
        results.append("0")
    else:
        results.append("1")
            
print("\n".join(results) + "\n")


