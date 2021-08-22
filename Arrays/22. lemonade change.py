# Problem Disc: https://leetcode.com/problems/lemonade-change/

def solve(bills):
    change = {5:0, 10:0}
    for i in range(len(bills)):
        if bills[i] == 5:
            change[5] += 1

        elif bills[i] == 10:
            if change[5] > 0:
                change[5] -= 1
                change[10] += 1
            else:
                return False

        elif bills[i] == 20:
            if change[5] > 0 and change[10] > 0:
                change[5] -= 1
                change[10] -= 1
            elif change[5] >= 3:
                change[5] -= 3
            else:
                return False
            
    return True

bills = [5,5,5,10,5,5,10,20,20,20]
print(solve(bills))


def solve(bills):
    fiveCoins = tenCoins = 0
    for x in bills:
        if x == 5:
            fiveCoins += 1
        elif x == 10:
            if not fiveCoins:
                return False
            fiveCoins -= 1
            tenCoins += 1
        elif x == 20:
            if fiveCoins and tenCoins:
                fiveCoins -= 1
                tenCoins -= 1
            elif fiveCoins >= 3:
                fiveCoins -= 3
            else:
                return False
    return True

bills = [5,5,10,10,20]
print(solve(bills))

