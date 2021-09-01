# Problem Disc: https://leetcode.com/problems/container-with-most-water/

# Method 1: BruteForce 
def solve(height):
    n = len(height)
    maxWater = 0
    for i in range(n):
        for j in range(i+1, n):
            if height[j] <= height[i]:
                water = height[j]*(j-i)
                if water > maxWater:
                    maxWater = water
    return maxWater

height = [1,8,6,2,5,4,8,3,7]
print(solve(height))


# Meethod 2: Two Pointer Technique
def solve(height):
    i, j = 0, len(height)-1
    maxWater = 0
    while i < j:
        water = min(height[i], height[j]) * (j-i)
        maxWater = max(maxWater, water)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxWater

print(solve(height))