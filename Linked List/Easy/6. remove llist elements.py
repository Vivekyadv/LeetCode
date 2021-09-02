# Problem Statement: https://leetcode.com/problems/remove-linked-list-elements/


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

def printf(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

def remove(head, val):
    if head is None or (head.next is None and head.val == val):
        return None

    result = ListNode()
    result.next = head
    prev = result
    curr = result.next
    while curr:
        if curr.val == val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = prev.next
            curr = curr.next
    
    return result.next


l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(8)

printf(l1)
printf(remove(l1, 3))
