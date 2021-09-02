# Problem statement: https://leetcode.com/problems/reverse-linked-list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
def printf(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()  
    
def reverse(head):
    prev = None
    curr = head
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt

    return prev

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(8)

printf(l1)
printf(reverse(l1))