# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            p, q = stack.pop()

            if p == None or q == None:
                if p == q:
                    continue

                return False

            if p.val != q.val:
                return False

            stack.extend([(p.left, q.left), (p.right, q.right)])

        return True
