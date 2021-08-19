# Problem Disc: https://leetcode.com/problems/degree-of-an-array/

from collections import Counter
def solve(arr):
    counter = Counter(arr)
    deg = max(counter.values())
    
    max_ele = []
    for x in counter.keys():
        if counter[x] == deg:
            max_ele.append(x)
    
    min_len = len(arr)
    for x in max_ele:
        s = arr.index(x)
        e = len(arr) - arr[::-1].index(x)
        if e-s < min_len:
            min_len = e-s
    return min_len

print(solve([1,2,2,3,2,4,1]))


def solve(arr):
    store = {}
    n = len(arr)
    for i in range(n):
        if arr[i] not in store:
            store[arr[i]] = [1, i, i]
        else:
            store[arr[i]][0] += 1
            store[arr[i]][2] = i
    
    deg = 0
    for x in store.keys():
        if store[x][0] > deg:
            deg = store[x][0]

    res = n
    for x in store:
        if store[x][0] == deg:
            res = min(res, store[x][-1] - store[x][1])
    return res+1

arr = [1,1,2,2,3,2,4]
print(solve(arr))


def solve(arr):
    s, e, store = {}, {}, {}
    for i, x in enumerate(arr):
        if x not in store:
            store[x] = 1
            s[x] = e[x] = i
        else:
            store[x] += 1
            e[x] = i

    degree = max(store.values())
    minLen = len(arr)
    for x in store:
        if store[x] == degree:
            minLen = min(minLen, e[x]-s[x]+1)
    return minLen

print(solve(arr))