# add two numbers represented as linked list


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

def printf(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

def Reverse_List(head):
    prev = None
    curr = head
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    
    return prev

def add(l1, l2):

    result = ListNode(0)
    ptr = result
    carry = 0
    while l1 or l2:
        a = 0 if l1 is None else l1.val
        b = 0 if l2 is None else l2.val

        Sum = a + b + carry
        ptr.next = ListNode(Sum % 10)
        carry = Sum // 10
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        ptr = ptr.next

    if carry:
        ptr.next = ListNode(carry)

    return result.next


l1 = ListNode(5)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(8)

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(6)

printf(l1)
printf(l2)
printf(add(l1, l2))

res = Reverse_List(l1)
printf(res)