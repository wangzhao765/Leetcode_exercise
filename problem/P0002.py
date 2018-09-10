# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        list1 = []
        while p != None:
            list1.append(p.val)
            p = p.next
        p = l2
        list2 = []
        while p !=None:
            list2.append(p.val)
            p = p.next
        m = 0
        n = 0
        add = 0
        ans = []
        while m < len(list1) or n < len(list2):
            if m < len(list1):
                add += list1[m]
            if n < len(list2):
                add += list2[n]
            ans.append(add % 10)
            add //= 10
            m += 1
            n += 1
        if add > 0:
            ans.append(add)
        a = ListNode(ans[0])
        b = a
        for i in range(1, len(ans), 1):
            c = ListNode(ans[i])
            b.next = c
            b = c
        return a

s = Solution()
a = ListNode(1)
b = a
for i in range(10):
    c = ListNode(i)
    b.next = c
    b = c
s.addTwoNumbers(a, a)
