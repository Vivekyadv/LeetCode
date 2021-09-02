# Problem Statement: https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
def printf(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()  

def solve(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr == arr[::-1]

# Method 2: Reverse the right half and check for palindrome
def solve(head):
    if head is None or head.next is None:
        return True
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = slow
    curr = slow.next
    prev.next = None
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    
    ptr1 = head
    ptr2 = prev
    while ptr2:
        if ptr1.val != ptr2.val:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(1)


printf(l1)
print(solve(l1))
