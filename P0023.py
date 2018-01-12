# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        element = []
        i = 0
        for node in lists:
            if node!=None and node!=[]:
                element.append([node.val, i])
            i = i + 1
        element.sort(key=lambda x:x[0])
        answer = ListNode(0)
        nextnode = answer
        while len(element)>0:
            print(element[0][0])
            nextnode.next = ListNode(element[0][0])
            nextnode = nextnode.next
            lists[element[0][1]]=lists[element[0][1]].next
            if lists[element[0][1]]!=None:
                temp = [lists[element[0][1]].val, element[0][1]]
                i = 0
                while i<len(element) and element[i][0]<temp[0]:
                    i = i + 1
                element.insert(i, temp)
            element.pop(0)
        return answer.next

if __name__ == '__main__':
    s = Solution()
    lists = []
    a = ListNode(1)
    a1 = a
    a1.next = ListNode(3)
    a1 = a1.next
    a1.next = ListNode(5)
    lists.append(a)
    b = ListNode(1)
    b1 = b
    b1.next = ListNode(2)
    b1 = b1.next
    b1.next = ListNode(3)
    lists.append(b)
    c = ListNode(2)
    c1 = c
    c1.next = ListNode(4)
    c1 = c1.next
    c1.next = ListNode(6)
    lists.append(c)
    s.mergeKLists(lists)
