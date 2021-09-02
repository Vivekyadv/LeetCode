# Problem Statement: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

def printf(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

def length(head):
    leng = 0
    while head:
        leng += 1
        head = head.next
    return leng

# Method 1: multiply each binary integer with pow(2,i)
def solve(head):
    i = length(head)-1
    dec = 0
    while head:
        dec += head.val * pow(2,i)
        i -= 1
        head = head.next
    return dec

# Directly calculate without using i
def solve2(head):
    dec = 0
    while head:
        dec = dec * 2 + head.val
        head = head.next
    return dec


l1 = ListNode(1)
l1.next = ListNode(0)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(1)
l1.next.next.next.next = ListNode(1)

printf(l1)
print(solve(l1))
print(solve2(l1))
