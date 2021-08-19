# Given prices of stocks on each day, you have to maximise the profit. You can buy and sell
# stocks multiple times. But can't have multiple transactions simultaneously 

# Arr = [7,1,5,3,6,4,2,10] -> (1,5) and (3,6) and (2,10) -> total profit = 15

# Valley-Peak approach
# buy at valley and sell at peak

def solve(arr, n):
    profit = 0
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            profit += arr[i] - arr[i-1]
    return profit

arr = [7,1,5,3,6,4,2,10]
print(solve(arr, len(arr))) 
