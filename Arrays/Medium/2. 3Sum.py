# Problem disc: https://leetcode.com/problems/3sum/

def solve(arr):
    n = len(arr)
    arr.sort()
    if n < 3:
        return []
    store = {}
    for i in range(n-2):
        j, k = i+1, n-1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total == 0:
                temp = sorted([arr[i], arr[j], arr[k]])
                store[tuple(temp)] = 1
                j += 1
                k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1
    return [list(key) for key in store]

arr = [-1,0,1,2,-1,-4]
print(solve(arr))
