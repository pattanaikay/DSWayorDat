class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            temp_curr = curr.next

            curr.next = prev

            prev = curr
            curr = temp_curr
        
        return prev