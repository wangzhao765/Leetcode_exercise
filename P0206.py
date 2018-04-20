# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        ans = []
        node = head
        while node!=None:
            ans.append(node)
            node = node.next
        print(ans)
        if len(ans)==1:
            return ans[0]
        newhead = ans[-1]
        newnode = newhead
        for i in range(len(ans)-2, -1, -1):
            print(i, ans[i].val)
            newnode.next = ans[i]
            newnode = newnode.next
        newnode.next=None
        return newhead

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    head.next = a
    a.next = b
    b.next = c
    newhead = s.reverseList(head)
    while newhead!=None:
        print(newhead.val)
        newhead = newhead.next