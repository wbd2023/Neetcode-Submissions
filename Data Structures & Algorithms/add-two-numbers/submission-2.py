# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Assumes the returned list is not counted towards the O(1) space requirement.
        dummy = ListNode()
        previous = dummy

        # Since each node contains a single digit, `carry` can only be `0` or `1`.
        carry = 0

        while l1 or l2:
            total = carry
            total = total + l1.val if l1 else total
            total = total + l2.val if l2 else total

            carry, digit = divmod(total, 10)

            previous.next = ListNode(digit)
            previous = previous.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry:
            previous.next = ListNode(carry)

        return dummy.next

