# Problem Disc: https://leetcode.com/problems/1-bit-and-2-bit-characters/

def solve(arr):
    res = True
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            res = False
            i += 2
        else:
            res = True
            i += 1
    return res

arr = [1,1,0,0,1,0,0]
print(solve(arr))


def solve(arr):
    i = 0
    while i < len(arr)-1:
        i += 2 if arr[i] == 1 else 1
    return i != len(arr)

print(solve(arr))
