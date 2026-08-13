# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue, q_queue = [p], [q]

        while p_queue and q_queue:
            p, q = p_queue.pop(), q_queue.pop()

            if p == None or q == None:
                if p == q:
                    continue

                return False

            if p.val != q.val:
                return False

            p_queue.extend([p.left, p.right])
            q_queue.extend([q.left, q.right])

        return True if not p_queue and not q_queue else False
