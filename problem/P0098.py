# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return Solution.search(self, root, None, None)

    def search(self, root, l, r):
        ans = True
        if root.left!=None:
            if root.left.val>=root.val or (l!=None and root.left.val<=l):
                return False
            else:
                ans = ans and Solution.search(self, root.left, l, root.val)
        if root.right!=None:
            if root.right.val<=root.val or (r!=None and root.right.val>=r):
                return False
            else:
                ans = ans and Solution.search(self, root.right, root.val, r)
        return ans

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10)
    a = TreeNode(5)
    b = TreeNode(15)
    c = TreeNode(6)
    d = TreeNode(20)
    root.left = a
    root.right = b
    b.left = c
    b.right = d
    print(s.isValidBST(root))