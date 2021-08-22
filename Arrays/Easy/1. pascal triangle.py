# Given n, print all rows till n of pascal triangle


def solve(n):
    result = []
    prev = 1
    for i in range(1, n+1):
        result.append(prev)
        prev = prev*(n-i)//i
    return result

print(solve(5))

# Method 1: Brute Force
def solve(n):
    result = []
    prev = [1]
    for i in range(n):
        result.append(prev)
        prev = nextRow(prev)
    return result

def nextRow(row):
    ans = [1]
    for i in range(len(row)-1):
        ans.append(row[i] + row[i+1])
    ans.append(1)
    return ans

print(solve(5))


# Method 2:
def solve(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1,1]]

    ans = [[1], [1,1]]
    row = []
    i = 1
    while i < n-1:
        row.append(1)
        for j in range(len(ans[i])-1):
            row.append(ans[i][j] + ans[i][j+1])
        row.append(1)

        ans.append(row)
        row = []
        i += 1
    return ans

print(solve(5))


# When rth row and cth column is given, and asked to find the value 
def solve(r,c):
    res = 1
    for i in range(1, c):
        res = res*(r-i)//i
    return res

print(solve(5,3))
