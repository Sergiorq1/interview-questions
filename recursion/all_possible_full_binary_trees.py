# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int):
        # if n is an even number, there's no possibe FBT, a node in tree will always have a single child node
        if not n % 2:
            return []
        # if n = 1, then only one possible binary tree
        elif n == 1:
            return [TreeNode(0)]
        else:
            return [
                # nodes always have the value of 0
                TreeNode(0, left=lt, right=rt)
                # i starts at 1, ends at value of n, but counts like 1,3,5,7, etc.
                for i in range(1, n, 2)
                # assigns tree to left node
                for lt in self.allPossibleFBT(i)
                # assigns tree to right node
                for rt in self.allPossibleFBT(n - 1 - i)
            ]

sol = Solution()
print(sol.allPossibleFBT(7))