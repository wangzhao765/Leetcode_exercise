# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = []
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.ans = [root.val, 0]
        Solution.search(self, root, 0)
        return Solution.ans[0]

    def search(self, root, level):
        if root.left==None and root.right==None:
            if level>Solution.ans[1]:
                Solution.ans[0] = root.val
                Solution.ans[1] = level
        else:
            if root.left!=None:
                Solution.search(self, root.left, level+1)
            if root.right!=None:
                Solution.search(self, root.right, level+1)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)
    root.left = a
    root.right = b
    a.left = c
    b.left = d
    b.right = e
    d.left = f
    print(s.findBottomLeftValue(root))