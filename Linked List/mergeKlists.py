class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next                
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            current.next = l1 if l1 else l2
            return dummy.next
        
        def mergeKListsHelper(start, end):
            if start == end:
                return lists[start]
            if start + 1 == end:
                return mergeTwoLists(lists[start], lists[end])
            
            mid =  (start + end) // 2
            left = mergeKListsHelper(start, mid)
            right = mergeKListsHelper(mid + 1, end)

            return mergeTwoLists(left, right)
        
        return mergeKListsHelper(0, len(lists)-1)