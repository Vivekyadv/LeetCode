# Problem Statement: https://leetcode.com/problems/middle-of-the-linked-list/


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

def printf(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

def middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(15)
l1.next.next.next.next.next = ListNode(13)

printf(l1)
printf(middle(l1))
