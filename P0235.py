# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        if p.val<q.val:
            return Solution.search(self, root, p, q)
        else:
            return Solution.search(self, root, q, p)

    def search(self, root, p, q):
        if root.val>=p.val and root.val<=q.val:
            return root
        if root.val>=p.val and root.val>=q.val:
            return Solution.search(self, root.left, p, q)
        if root.val<=p.val and root.val<=q.val:
            return Solution.search(self, root.right, p, q)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(6)
    a = TreeNode(2)
    b = TreeNode(8)
    c = TreeNode(0)
    d = TreeNode(4)
    e = TreeNode(7)
    f = TreeNode(9)
    g = TreeNode(3)
    h = TreeNode(5)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    d.left = g
    d.right = h
    print(s.lowestCommonAncestor(root, d, a).val)