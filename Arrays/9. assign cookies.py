# problem discription: https://leetcode.com/problems/assign-cookies/

# Two pointer approach
def solve(g, s):
    g.sort()
    s.sort()
    m = len(g)
    n = len(s)
    count = 0
    i = j = 0
    while i < m and j < n:
        if g[i] <= s[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

g = [1,2]
s = [1,2,3]
print(solve(g, s))