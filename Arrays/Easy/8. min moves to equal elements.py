# problem statement: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

# Approach:
# 1. sort the array
# 2. till all elements are not equal, increment all n-1 elements
# 3. since arr is sorted, max element never get incremented

def solve(arr):
    arr.sort()
    n = len(arr)
    count = 0

    while arr[-1]*n != sum(arr):
        for i in range(n-1):
            arr[i] += 1
        count += 1
        arr.sort()
    return count

arr = [1,1,2,2,3]
print(solve(arr))
# TLE


# Method 2:
# Instead of incrementing n-1 elements, we can decrease 1 element (dec max element)
# [1,2,5,4,2,3,1]
def solve(arr, n):
    count = 0
    minEle = min(arr)
    for i in range(n):
        count += arr[i] - minEle
    return count

arr = [1,2,5,4,2,3,1]
print(solve(arr, len(arr)))

# Modified method 2
# Formula = sum(arr) - n*min(arr)
def solve(arr, n):
    minEle = min(arr)
    total = sum(arr)
    return total - n*minEle

