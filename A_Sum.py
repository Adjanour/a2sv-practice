num_tests = int(input())

for _ in range(num_tests):
    #  number of elements is three
    arr = list(map(int, input().split()))

    total_sum = sum(arr)
    if arr[0] == total_sum - arr[0]:
        print("YES")
    elif arr[1] == total_sum - arr[1]:
        print("YES")
    elif arr[2] == total_sum - arr[2]:
        print("YES")
    else:        
        print("NO")