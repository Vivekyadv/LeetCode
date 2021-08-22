# Problem disc: https://leetcode.com/problems/reshape-the-matrix/

# Reshape the matrix in rXc matrix

def solve(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    if r*c != m*n or r == m or c == n:
        return mat

    store = [mat[i][j] for i in range(m) for j in range(n)]
    ans = [[0 for j in range(c)] for i in range(r)]
    k = 0
    for i in range(r):
        for j in range(c):
            ans[i][j] = store[k]
            k += 1
    return ans

mat = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
r = 5
c = 3
print(solve(mat,r,c))
