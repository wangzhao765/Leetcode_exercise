# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        h1 = h
        while h1.next != None and h1.next.next != None:
            temp = h1.next
            h1.next = h1.next.next
            temp.next = h1.next.next
            h1.next.next = temp
            h1 = h1.next.next
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
    k = s.swapPairs(a)
    while k!=None:
        print(k.val)
        k = k.next
