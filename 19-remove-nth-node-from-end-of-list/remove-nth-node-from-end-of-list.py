# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        length =0

        while current:
            length +=1
            current = current.next
        
        pos = length-n

        if pos ==0:
            return head.next

        current = head

        for _ in range(pos-1):
            current = current.next
        current.next = current.next.next
        return head


