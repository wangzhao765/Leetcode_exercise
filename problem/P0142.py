# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast!=None:
            fast=fast.next
            if fast==None:
                break
            fast=fast.next
            slow=slow.next
            if fast==slow:
                break
        if fast==None:
            return None
        begin = head
        while begin!=fast:
            begin=begin.next
            fast=fast.next
        return begin

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    e = ListNode(6)
    head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c
    begin = s.detectCycle(head)
    print(begin.val)