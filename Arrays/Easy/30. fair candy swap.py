# Problem disc: https://leetcode.com/problems/fair-candy-swap/

def solve(alice, bob):
    Sa = sum(alice)
    Sb = sum(bob)
    bobSet = set(bob)
    for x in alice:
        y = x + (Sb-Sa)//2
        if y in bobSet:
            return [x, y]


def solve(alice, bob):
    Sa = sum(alice)
    Sb = sum(bob)
    
    target = (Sa + Sb) // 2
    alice_need = target - Sa
    bob_set = set(bob)
    
    for x in alice:
        y = x + alice_need
        if y in bob_set:
            return [x, y]


# Problem 2: Smallest Range I
# Problem Disc: https://leetcode.com/problems/smallest-range-i/

def solve(arr, k):
    miN = min(arr) + k
    maX = max(arr) - k
    if miN > maX:
        return 0
    else:
        return maX - miN

# OR
#    return max(0, (max(nums) - k) - (min(nums) + k))
