
# Method 1: Time = 1036 ms and Space = 21.9 MB
# Time Complexity -> O(nlogn)
# Space Complexity -> O(n)

def BS(arr, key):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = l + (h-l)//2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            l = mid + 1
        else:
            h = mid - 1
    return 0

def solve(arr):
    n = len(arr)
    arr.sort()
    res = []
    for i in range(1, n+1):
        if BS(arr, i) == 0:
            res.append(i)
    return res

arr = [4,3,2,7,8,2,3,1]
print(solve(arr))


# Method 2: Time = 336  ms and Space = 21.8 MB
# Time Complexity -> O(n)
# Space Complexity -> O(n)
def solve(arr, n):
    temp = [0]*(n)
    for i in arr:
        temp[i-1] = 1
    
    res = []
    for i in range(n):
        if temp[i] == 0:
            res.append(i+1)
    return res

print(solve(arr, len(arr)))


# Method 3: Negative marking
def solve(arr, n):
    for num in arr:
        num = abs(num)
        if num <= n and arr[num-1] > 0:
            arr[num-1] *= -1
    
    res = []
    for i in range(n):
        if arr[i] > 0:
            res.append(i+1)
    return res

arr = [4,3,2,7,8,2,3,1]
print(solve(arr, len(arr)))
