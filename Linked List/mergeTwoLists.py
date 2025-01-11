class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initializing dummy variable to avoid edge cases
        dummy = ListNode(0)
        current = dummy

        # compare and merge when both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.nxt
        
        current.next = list1 if list1 else list2
        
        return dummy.next