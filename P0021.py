# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = l1
        list2 = l2
        answer = ListNode(0)
        next = answer
        while list1 != None and list2 != None:
            if list1.val<=list2.val:
                next.next = ListNode(list1.val)
                next = next.next
                list1 = list1.next
            else:
                next.next = ListNode(list2.val)
                next = next.next
                list2 = list2.next
        if list1 == None:
            temp = list2
        else:
            temp = list1
        while temp != None:
            next.next = ListNode(temp.val)
            next = next.next
            temp = temp.next
        return answer.next


if __name__ == '__main__':
    head1 = ListNode(1)
    next1 = head1
    next1.next = ListNode(2)
    next1 = next1.next
    next1.next = ListNode(4)
    head2 = ListNode(1)
    next2 = head2
    next2.next = ListNode(3)
    next2 = next2.next
    next2.next = ListNode(4)
    s = Solution()
    ans = s.mergeTwoLists(head1, head2)
    while ans != None:
        print(ans.val)
        ans = ans.next