class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # 1. Find length
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # 2. Avoid unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # 3. Make linked list circular
        tail.next = head

        # 4. Find new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # 5. New head is next of new tail
        new_head = new_tail.next

        # 6. Break the circle
        new_tail.next = None

        return new_head