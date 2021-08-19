# Problem Discription: 
def solve(grid):
    peri = 0
                
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                peri += 4
                if i > 0 and grid[i-1][j]:
                    peri -= 2
                if j > 0 and grid[i][j-1]:
                    peri -= 2
    return peri             

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(solve(grid))


# Method 2:
def solve(grid):
    peri = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                peri += 4
                row = i and grid[i-1][j]
                colm = j and grid[i][j - 1]
                peri -= (2*row + 2*colm)
    return peri

print(solve(grid))