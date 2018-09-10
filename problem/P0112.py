# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        return Solution.search(self, root, 0, sum)

    def search(self, root, sum, target):
        ans = False
        if root.left!=None:
            ans = ans or Solution.search(self, root.left, sum+root.val, target)
        if root.right!=None:
            ans = ans or Solution.search(self, root.right, sum+root.val, target)
        if root.left==None and root.right==None:
            if sum+root.val==target:
                return True
            else:
                return False
        return ans

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    a = TreeNode(4)
    b = TreeNode(8)
    c = TreeNode(11)
    d = TreeNode(13)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(2)
    h = TreeNode(1)
    root.left = a
    root.right = b
    a.left = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.right = h
    print(s.hasPathSum(root, 22))