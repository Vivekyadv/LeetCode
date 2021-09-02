# Problem Statement: https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    sort = ListNode(0)
    ptr = sort
    while l1 and l2:
        if l1.val < l2.val:
            ptr.next = l1
            l1 = l1.next
        else:
            ptr.next = l2
            l2 = l2.next
        ptr = ptr.next
    
    if l1:
        ptr.next = l1
    elif l2:
        ptr.next = l2

    return sort.next

def printf(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

result = merge(l1, l2)
printf(result)
