# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        else:
            return Solution.search(self, root.left, root.right)

    def search(self, lroot, rroot):
        if lroot==None and rroot==None:
            return True
        elif (lroot==None and rroot!=None) or (lroot!=None and rroot==None):
            return False
        elif lroot.val!=rroot.val:
            return False
        else:
            return True and Solution.search(self, lroot.left, rroot.right) and Solution.search(self, lroot.right, rroot.left)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(3)
    f = TreeNode(3)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    print(s.isSymmetric(root))