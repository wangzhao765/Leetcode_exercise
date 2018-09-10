# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        node1 = head
        node2 = head
        while True:
            node1 = node1.next
            if not node1:
                return False
            node2 = node2.next
            if not node2:
                return False
            node2 = node2.next
            if not node2:
                return False
            if node1 == node2:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(s.hasCycle(head))