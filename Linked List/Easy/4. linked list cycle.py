# Problem Statement: https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Method 1: O(1) space
def solve(head):
    while head:
        if head.val is None:
            return True
        head.val = None
        head = head.next
    return False


# Method 2: 
def solve(head):
    if head is None or head.next is None:
        return False

    p = head
    q = head.next
    while p != None and q.next != None:
        p = p.next
        q = q.next
        if q is None:
            return False
        q = q.next
        if p == q:
            return True
        if q is None:
            return False
    return False


n1 = ListNode(5)
n2 = ListNode(6)
n3 = ListNode(2)
n4 = ListNode(13)

l = n1
l.next = n2
l.next.next = n3
l.next.next.next = n4
l.next.next.next.next = n2

print(solve(l))