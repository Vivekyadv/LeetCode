# Problem Statement: https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

def printf(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

def delete(node):
    prev = node
    curr = node.next
    prev.val = curr.val
    prev.next = curr.next
    curr.next = None

n1 = ListNode(3)
n2 = ListNode(0)
n3 = ListNode(4)
n4 = ListNode(11)
n5 = ListNode(9)

l1 = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

node = n3
printf(l1)
delete(node)
printf(l1)
