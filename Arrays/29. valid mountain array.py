# Problem disc: https://leetcode.com/problems/valid-mountain-array/

def solve(arr):
    if len(arr) < 3:
        return False
    
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            break
    
    peak = i
    if peak == 0 or peak == len(arr)-1:
        return False
    
    for i in range(peak, len(arr)-1):
        if arr[i] <= arr[i+1]:
            return False
    return True


def solve(arr):
    n = len(arr)
    if n < 3:
        return False
    i = 0
    while i+1 < n and arr[i] < arr[i+1]:
        i += 1
    
    if i == 0 or i == n-1:
        return False
    
    while i+1 < n and arr[i] > arr[i+1]:
        i += 1
    
    return i == n-1