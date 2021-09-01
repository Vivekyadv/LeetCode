# Problem disc: https://leetcode.com/problems/3sum-closest/

def solve(arr, target):
    arr.sort()
    minSum = sum(arr[:3])
    minDiff = float('inf')
    for i in range(len(arr)-2):
        j, k = i+1, len(arr)-1
        while j < k:
            currSum = arr[i] + arr[j] + arr[k]
            if abs(currSum - target) < minDiff:
                minDiff = abs(currSum - target)
                minSum = currSum
            if currSum < target:
                j += 1
            elif currSum > target:
                k -= 1
            else:
                return currSum
    return minSum
