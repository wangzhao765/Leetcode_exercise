# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        h1 = h
        h2 = h
        flag = True
        for i in range(k):
            if h2.next != None:
                h2 = h2.next
            else:
                flag = False
                break
        while flag:
            h3 = h1
            temp = h3.next
            for i in range(k-1):
                temp2 = temp.next
                temp.next = temp2.next
                temp2.next = h3.next
                h3.next = temp2
            h1 = temp
            h2 = h1
            for i in range(k):
                if h2.next != None:
                    h2 = h2.next
                else:
                    flag = False
                    break
        return h.next

if __name__ == '__main__':
    s = Solution()
    a = ListNode(1)
    a1 = a
    a1.next = ListNode(2)
    a1 = a1.next
    a1.next = ListNode(3)
    a1 = a1.next
    a1.next = ListNode(4)
    a1 = a1.next
    a1.next = ListNode(5)
    ans = s.reverseKGroup(a, 4)
    while ans!=None:
        print(ans.val)
        ans = ans.next
