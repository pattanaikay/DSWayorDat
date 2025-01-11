class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            while not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next

        return True