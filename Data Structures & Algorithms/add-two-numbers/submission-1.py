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

        # Assumes `l1` and `l2` are the same length.
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry, digit = divmod(total, 10)

            previous.next = ListNode(digit)
            previous = previous.next

            l1 = l1.next
            l2 = l2.next

        if carry:
            previous.next = ListNode(carry)

        return dummy.next

    def length(self, head: Optional[ListNode]) -> int:
        length = 0

        while head:
            head = head.next
            length += 1

        return length
