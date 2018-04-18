# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0;
        p, m=Solution.search(self, root)
        return m

    def search(self, root):
        if root.left==None and root.right==None:
            return root.val, root.val
        p = -99999999
        m = root.val
        lm = -99999999
        rm = -99999999
        if root.left!=None:
            lp, lm = Solution.search(self, root.left)
            p = max(p, lp+root.val)
            if lp>0:
                m = m + lp
        if root.right!=None:
            rp, rm = Solution.search(self, root.right)
            p = max(p, rp+root.val)
            if rp>0:
                m = m + rp
        return max(p, root.val), max(root.val, m, lm, rm)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    a = TreeNode(-2)
    b = TreeNode(3)
    root.left = a
    root.right = b
    print(s.maxPathSum(root))