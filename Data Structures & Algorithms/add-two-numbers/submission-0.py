# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Assumes list1 and list2 are of the same size.
        #
        # Assumes O(1) recommended constant time doesn't include results list.
        #
        # Note: since l1 and l2 are guaranteed to be single digit,
        # we only need to check for a max of a 1 value carried over since max total is 18.

        dummy = ListNode()
        previous = dummy
        carry = False

        while l1 and l2:
            total = l1.val + l2.val

            if carry:
                total += 1
                carry = False

            if total > 10:
                total -= 10
                carry = True

            node = ListNode(total)
            previous.next = node
            previous = node

            l1 = l1.next
            l2 = l2.next

        if carry:
            node = ListNode(1)
            previous.next = node
            previous = node

        return dummy.next
