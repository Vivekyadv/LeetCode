
# [0,1,2,4,5,7]   ->  [0,2], [4,5], [7,7]  ->  ["0->2", "4->5", "7"]

def solve(arr):
    start = end = 0
    arr.append("@")
    n = len(arr)
    ans = []
    for i in range(n-1):
        if arr[i] + 1 != arr[i+1]:
            end = i
            if start != end:
                temp = str(arr[start]) + "->" + str(arr[end])
                ans.append(temp)
            else:
                ans.append(str(arr[start]))
            start = i+1
    return ans

arr = [0,1,2,4,5,7]
print(solve(arr))


# Method 2: using while loop
def create_str(i, j):
    if i == j:
        return str(arr[i])
    else:
        return str(arr[i]) + "->" + str(arr[j])

def solve(arr):
    n = len(arr)
    i, j = 0, 0
    res = []
    while j < n-1:
        if arr[j + 1] == arr[j] + 1:
            j += 1
            continue
        res.append(create_str(i, j))
        j += 1
        i = j
    res.append(create_str(i, j))
    return res

arr = [0,1,2,4,5,7]
print(solve(arr))

