class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head 
        
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        else:
            return None
        
        slow = head 
        while slow!=fast:
            slow = slow.next
            fast= fast.next
        return slow  
            