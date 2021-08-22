# Problem disc: https://leetcode.com/problems/flood-fill/

def solve(img, sr, sc, newColor):
    color = img[sr][sc]
    if color == newColor:
        return img
    
    dfs(sr, sc, color)
    return img

def dfs(i, j, color):
    img[i][j] = newColor
    if i-1 >= 0 and img[i-1][j] == color:
        dfs(i-1, j, color)
    if j+1 < m and img[i][j+1] == color:
        dfs(i, j+1, color)
    if i+1 < n and img[i+1][j] == color:
        dfs(i+1, j, color)
    if j-1 >= 0 and img[i][j-1] == color:
        dfs(i, j-1, color)
    return

img = [[1,2,1,1],[2,1,1,2],[1,0,1,0]]
newColor = 3
n, m = len(img), len(img[0])
print(solve(img, 1, 2, newColor))