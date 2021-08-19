# problem disc: https://leetcode.com/problems/max-consecutive-ones/

def solve(arr):
    i = j = 0
    res = 0
    while j < len(arr):
        if arr[j] == 1:
            j += 1
            res = max(res, j-i)
        else:
            j += 1
            i = j
    return res

arr = [1,0,1,1,1,0,1]
print(solve(arr))


def solve(arr):
    count = res = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            res = max(res, count)
        else:
            count = 0
    return res

print(solve(arr))