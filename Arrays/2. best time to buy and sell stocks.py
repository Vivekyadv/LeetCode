
def solve(arr):
    n = len(arr)
    minSoFar = arr[0]
    profit = 0
    for i in range(n):
        if arr[i] < minSoFar:
            minSoFar = arr[i]
        if arr[i] - minSoFar > profit:
            profit = arr[i] - minSoFar
    return profit

arr = [7,1,5,4,6,3]
print(solve(arr))
