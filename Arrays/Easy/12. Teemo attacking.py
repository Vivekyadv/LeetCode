# Problem disc: https://leetcode.com/problems/teemo-attacking/ 

def solve(timeSeries, duration):
    counter = set()
    for i in range(len(timeSeries)):
        num = timeSeries[i]
        for x in range(num, num+duration):
            counter.add(x)
    return len(counter)

arr = [1,4]
time = 2 
print(solve(arr, time))
# Time = O(n^2)
# Space = O(n)

# Method 2:
def solve(timeSeries, duration):
    endTime = 0
    res = 0
    for time in timeSeries:
        if endTime > time:
            res -= (endTime-time)
        res += duration
        endTime = time + duration
    return res

arr = [1,2,5,8,12]
print(solve(arr, 2))

# OR 
# res += min(duration,, arr[i+1]-arr[i])
