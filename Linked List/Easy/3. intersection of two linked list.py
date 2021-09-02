# Problem Statement: https://leetcode.com/problems/intersection-of-two-linked-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def length(head):
    leng = 0
    while head:
        leng += 1
        head = head.next
    return leng

def intersection(l1, l2):
    if l1 is None or l2 is None:
        return None
    
    len1 = length(l1)
    len2 = length(l2)
    k = abs(len1 - len2)
    ptr1, ptr2 = l1, l2

    if len1 > len2:
        while k:
            ptr1 = ptr1.next
            k -= 1
    else:
        while k:
            ptr2 = ptr2.next
            k -= 1

    while ptr1 and ptr2:
        if ptr1 == ptr2:
            return ptr1
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return None

def printf(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

l1 = ListNode(4)
l1.next = ListNode(1)
l1.next.next = common

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(1)
l2.next.next.next = common

printf(l1)
printf(l2)

printf(intersection(l1, l2))
printf(intersection(l1, l2))