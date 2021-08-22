# Problem Disc: https://leetcode.com/problems/min-cost-climbing-stairs/

# Method 1: simple approach
# Take minimum of last two elements
def solve(cost):
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[-1], cost[-2])

cost = [1,10,10,5,2,1,1,12,1]
print(solve(cost))


def solve(cost):
    min1 = min2 = 0
    for i in range(len(cost)-1, -1, -1):
        temp = cost[i] + min(min1, min2)
        min2 = min1
        min1 = temp
    return min(min1, min2)

cost = [1,10,10,5,2,1,1,12,1]
print(solve(cost))