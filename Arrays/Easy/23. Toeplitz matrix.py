# problem disc: https://leetcode.com/problems/toeplitz-matrix/



def solve(matrix):
    n = len(matrix)
    for i in range(n-1):
        if matrix[i][:-1] != matrix[i+1][1:]:
                return False
    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(solve(matrix)) 

def solve(matrix):
    n = len(matrix)
    store = {}
    for i in range(n):
        for j, val in enumerate(matrix[i]):
            if i-j not in store:
                store[i-j] = val
            elif store[i-j] != val:
                return False
    return True

print(solve(matrix))


def solve(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(1,n):
        for j in range(1,m):
            if matrix[i-1][j-1] != matrix[i][j]:
                return False
    return True

print(solve(matrix))