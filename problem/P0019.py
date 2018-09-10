# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=head
        q=head
        i=0
        while i<n:
            p=p.next
            i += 1
        if p==None:
            q=head.next
            return q
        while p.next!=None:
            p=p.next
            q=q.next
        t=q.next.next
        q.next=t;
        r=head
        while r!=None:
            print(r.val)
            r=r.next
        return(head)



s=Solution()
head=ListNode(1)
point=head
# for i in range(2,6):
#     t=ListNode(i)
#     point.next=t
#     point=t
print(s.removeNthFromEnd(head,1))