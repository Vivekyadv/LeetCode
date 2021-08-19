# Problem disc: https://leetcode.com/problems/can-place-flowers/


def solve(arr, n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            prev = 0 if i == 0 or arr[i-1] == 0 else 1
            next = 0 if i == len(arr)-1 or arr[i+1] == 0 else 1

            if prev == 0 and next == 0:
                count += 1
                arr[i] = 1
    return n <= count

arr = [1,0,0,0,0,1]
print(solve(arr, 2))


def solve(arr, n):
    prev, m = 0, len(arr)
    for i in range(m):
        if arr[i] == 0:
            if prev == 0 and (i == m-1 or arr[i+1] == 0):
                n -= 1
                arr[i] = 1
        prev = arr[i]
    return n <= 0

arr = [1,0,0,0,0,1]
print(solve(arr, 2))