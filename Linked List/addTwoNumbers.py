class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            # getting values from the list (0 if list ended)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # calculate sum and carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            # create new node with calculated digit
            current.next = ListNode(digit)
            current = current.next

            # move to next digits if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next