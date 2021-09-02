# Problem Statement: https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove(head):
    if head is None or head.next is None:
        return head
    
    result = head
    prev = result
    nextt = result.next
    while nextt:
        if prev.val == nextt.val:
            prev.next = nextt.next
            nextt = nextt.next
        else:
            prev = nextt
            nextt = nextt.next
    
    return result

def printf(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(5)

printf(l1)
printf(remove(l1))