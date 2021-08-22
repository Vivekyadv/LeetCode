# Problem disc: https://leetcode.com/problems/projection-area-of-3d-shapes/

def solve(grid):
    top = result = 0
    n = len(grid)
    
    for i in range(n):
        side1_view = side2_view = 0
        for j in range(n):
            if grid[i][j] != 0:
                top += 1
            side1_view = max(side1_view, grid[i][j])
            side2_view = max(side2_view, grid[j][i])
        
        result += side1_view + side2_view
    return result + top 

grid = [[2,2,2],[2,1,2],[2,2,2]]
print(solve(grid))


def solve(grid):
    n = len(grid)
    top = n*n
    side1 = side2 = 0

    for i in range(n):
        side1 += max(grid[i])
        maxC = 0
        for j in range(n):
            if grid[j][i]:
                maxC = max(maxC, grid[j][i])
            else: top -= 1
        side2 += maxC
    return top + side1 + side2

print(solve(grid))
