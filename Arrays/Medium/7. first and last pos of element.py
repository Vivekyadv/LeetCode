# Problem disc: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def BinarySearch(arr, target, isFirst):
    indx = -1
    l, h = 0, len(arr)-1
    while l <= h:
        mid = l + (h-l)//2
        if arr[mid] == target:
            indx = mid
            if isFirst:
                h = mid - 1
            else:
                l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return indx


def solve(arr, target):
    first = BinarySearch(arr, target, True)
    last = BinarySearch(arr, target, False)
    return [first, last]

arr = [2,4,10,10,10,18,20]
print(solve(arr, 10))   
