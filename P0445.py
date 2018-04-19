# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a1 = Solution.search(self, l1)
        a2 = Solution.search(self, l2)
        i1 = len(a1)-1
        i2 = len(a2)-1
        ans = []
        while i1>=0 or i2>=0:
            t = 0;
            if i1>=0:
                t = t + a1[i1]
            if i2>=0:
                t = t + a2[i2]
            ans.append(t)
            i1 = i1-1
            i2 = i2-1
        for i in range(len(ans)):
            if i==len(ans)-1:
                if ans[i]>=10:
                    ans.append(ans[i]//10)
                ans[i] = ans[i]%10
                break
            else:
                ans[i+1] = ans[i+1] + ans[i]//10
                ans[i] = ans[i]%10
        if (len(ans)==1):
            root = ListNode(ans[0])
            return root
        root = ListNode(ans[-1])
        now = root
        for i in range(len(ans)-2, -1, -1):
            temp = ListNode(ans[i])
            now.next = temp
            now = now.next
        return root

    def search(self, l):
        ans = []
        while l!=None:
            ans.append(l.val)
            l = l.next
        return ans

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(7)
    l1a = ListNode(2)
    l1b = ListNode(4)
    l1c = ListNode(3)
    l1.next = l1a
    l1a.next = l1b
    l1b.next = l1c
    l2 = ListNode(0)
    # l2a = ListNode(6)
    # l2b = ListNode(4)
    # l2.next = l2a
    # l2a.next = l2b
    root = s.addTwoNumbers(l1, l2)
    while root!=None:
        print(root.val)
        root = root.next