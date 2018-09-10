# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Solution.ans = []
        if root==None:
            return Solution.ans
        Solution.search(self, root)
        return Solution.ans

    def search(self, root):
        if root.left!=None:
            Solution.search(self, root.left)
        Solution.ans.append(root.val)
        if root.right!=None:
            Solution.search(self, root.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    root.right = a
    a.left = b
    print(s.inorderTraversal(None))