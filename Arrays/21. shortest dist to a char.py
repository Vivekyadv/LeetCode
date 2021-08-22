# Problem Disc: https://leetcode.com/problems/shortest-distance-to-a-character/

# Method 1: Brute Force
def solve(string, char):
    index = []
    for i in range(len(string)):
        if string[i] == char:
            index.append(i)
    
    result = []
    for j in range(len(string)):
        indx = abs(j-index[0])
        for i in index:
            indx = min(indx, abs(j-i))
        result.append(indx)
    return result

string = "loveleetcode"
char = "e"
print(solve(string, char))


# Method 2: left check and right check
def solve(string, char):
    prev = float('-inf')
    result = []
    for i in range(len(string)):
        if string[i] == char:
            prev = i
        result.append(abs(i-prev))
    
    prev = float('inf')
    for i in range(len(string)-1, -1, -1):
        if string[i] == char:
            prev = i
        result[i] = min(result[i], abs(i-prev))
    return result

print(solve(string, char))