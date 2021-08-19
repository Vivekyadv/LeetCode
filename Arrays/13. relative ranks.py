# problem disc: https://leetcode.com/problems/relative-ranks/

def solve(score):
    tempArr = sorted(score, reverse=True)
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(len(score)):
        indx = score.index(tempArr[i])
        score[indx] = rank[i] if i < 3 else str(i+1)
    return score

score = [10,3,5,8,9,4]
print(solve(score))
# Time = O(n^2)
# Space = O(n)

# Method 2: using hashmap
def solve(score):
    tempArr = sorted(score, reverse=True)
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    store = {}
    for i in range(len(score)):
        store[tempArr[i]] = rank[i] if i < 3 else str(i+1)
    return [store[x] for x in score]

score = [10,3,5,8,9,4]
print(solve(score))
# Time = O(nlogn)
# Space = O(n)
