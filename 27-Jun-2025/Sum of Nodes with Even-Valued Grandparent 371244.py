# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not(root):
            return 0
        sum=0
        if root.val%2 == 0:
            if root.left:
                if root.left.left:
                    print(root.left.left.val)
                    sum+=root.left.left.val
                if root.left.right:
                    print(root.left.right.val)
                    sum+=root.left.right.val
            if root.right:
                if root.right.left:
                    print(root.right.left.val)
                    sum+=root.right.left.val
                if root.right.right:
                    print(root.right.right.val)
                    sum+=root.right.right.val
        return sum+self.sumEvenGrandparent(root.left)+self.sumEvenGrandparent(root.right)

