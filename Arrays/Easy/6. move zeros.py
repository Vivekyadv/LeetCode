# Input:  [0,1,0,3,12]
# Output: [1,3,12,0,0]

def solve(arr):
    n = len(arr)
    i = j = 0
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr

arr = [-2,0,-3,1,0,3,12]
print(solve(arr))
