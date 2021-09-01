# Problem disc: https://leetcode.com/problems/search-in-rotated-sorted-array

def solve(arr, target):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = l + (h-l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= arr[h]:
            if arr[mid] <= target and target <= arr[h]:
                l = mid + 1
            else:
                h = mid - 1
        else:
            if arr[l] <= target and target <= arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
    return -1

arr = [4,5,6,7,0,1,2]
target = 6
print(solve(arr, target))
