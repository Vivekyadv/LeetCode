# Problem disc : https://leetcode.com/problems/minimum-index-sum-of-two-lists/submissions/

def solve(list1, list2):
    uniq = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                uniq.append([i+j, list1[i]])
    miN = min(uniq)
    res = []
    for x in uniq:
        if x[0] == miN[0]:
            res.append(x[1])
    return res

list1 = ["Shogun","KFC","Tapioca Express","Burger King"]
list2 = ["KFC","Shogun", "Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse"]
print(solve(list1, list2))

# Time = O(n^2)
# Space = O(n)


# Method 2: using hashmap
def solve(l1, l2):
    store = {}
    for i in range(len(l1)):
        store[l1[i]] = i
    
    ans = []
    minIndx = 2**32
    Indx = 0

    for j in range(len(l2)):
        if l2[j] in store:
            Indx = j + store[l2[j]]
            if Indx < minIndx:
                ans.clear()
                ans.append(l2[j])
                minIndx = Indx
            elif Indx == minIndx:
                ans.append(l2[j])
    return ans

print(solve(list1, list2))
