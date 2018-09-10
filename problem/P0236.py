# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack1 = []
        stack1.append([root, 0])
        while len(stack1)>0:
            if stack1[-1][0]==p:
                break
            if stack1[-1][1]==0:
                stack1[-1][1] = 1
                if stack1[-1][0].left!=None:
                    stack1.append([stack1[-1][0].left, 0])
                continue
            if stack1[-1][1]==1:
                stack1[-1][1] = 2
                if stack1[-1][0].right!=None:
                    stack1.append([stack1[-1][0].right, 0])
                continue
            if stack1[-1][1]==2:
                del[stack1[-1]]
        stack2 = []
        stack2.append([root, 0])
        while len(stack2) > 0:
            if stack2[-1][0] == q:
                break
            if stack2[-1][1] == 0:
                stack2[-1][1] = 1
                if stack2[-1][0].left != None:
                    stack2.append([stack2[-1][0].left, 0])
                continue
            if stack2[-1][1] == 1:
                stack2[-1][1] = 2
                if stack2[-1][0].right != None:
                    stack2.append([stack2[-1][0].right, 0])
                continue
            if stack2[-1][1] == 2:
                del [stack2[-1]]
        index = 0;
        while index<len(stack1) and index<len(stack2) and stack1[index][0]==stack2[index][0]:
            index = index + 1
        return stack1[index-1][0]

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    a = TreeNode(5)
    b = TreeNode(1)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(0)
    f = TreeNode(8)
    g = TreeNode(7)
    h = TreeNode(4)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    d.left = g
    d.right = h
    print(s.lowestCommonAncestor(root, d, h).val)