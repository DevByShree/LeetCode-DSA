# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        pointers = lists

        dummy = ListNode(0)
        current = dummy

        while True:
            smallest = None
            smallest_i = -1

            for i in range(len(pointers)):
                if pointers[i]:

                    if smallest is None or pointers[i].val < smallest.val:
                        smallest = pointers[i]
                        smallest_i = i

            # for loop ke BAAD check karna hai
            if smallest is None:
                break

            current.next = smallest
            current = current.next

            pointers[smallest_i] = pointers[smallest_i].next

        return dummy.next