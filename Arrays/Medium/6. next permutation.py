# Problem disc: https://leetcode.com/problems/next-permutation/

def solve(arr):
    indx = -1
    n = len(arr)
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            indx = i
            break
    
    if indx == -1:
        return sorted(arr)
    
    for i in range(n-1, indx, -1):
        if arr[i] > arr[indx]:
            arr[i], arr[indx] = arr[indx], arr[i]
            break
    
    rev = arr[n-1:indx:-1]
    arr[:] = arr[:indx+1] + rev    
    return arr

arr = [1,2,3,5,4]
print(solve(arr))
