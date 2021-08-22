# Problem Disc: https://leetcode.com/problems/find-pivot-index/

# Method 1: Brute Force
def solve(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

arr = [1,7,3,6,5,6]
print(solve(arr))
# Time = O(n^2)


# Method 2: LeftSum and RightSum array
def solve(arr):
    n = len(arr)
    leftSum = [0]*n
    for i in range(1, n):
        leftSum[i] = leftSum[i-1] + arr[i-1]
    
    rightSum = [0]*n
    for i in range(n-2,-1,-1):
        rightSum[i] = rightSum[i+1] + arr[i+1]
    
    for i in range(n):
        if leftSum[i] == rightSum[i]:
            return i
    return -1

print(solve(arr))
# Time = O(n)
# Space = O(n)


# Method 3: Two pointer approach
def solve(arr):
    leftSum = 0
    rightSum = sum(arr)
    for i in range(len(arr)):
        rightSum -= arr[i]
        if leftSum == rightSum:
            return i
        leftSum += arr[i]
    return -1

print(solve(arr))
# Time = O(n)
# Space = O(1)