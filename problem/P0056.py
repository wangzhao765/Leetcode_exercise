# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        if len(intervals)==0:
            return ans
        que = []
        for node in intervals:
            que.append([node.start, "l"])
            que.append([node.end, "r"])
        que.sort()
        stack = []
        for node in que:
            if node[1]=="l":
                stack.append(node)
            if node[1]=="r":
                if len(stack)==1:
                    if len(ans)>0 and stack[0][0]==ans[-1].end:
                        ans[-1].end = node[0]
                    else:
                        ans.append(Interval(stack[0][0], node[0]))
                    stack = []
                else:
                    stack = stack[0:len(stack)-1]
        return ans

if __name__ == '__main__':
    s = Solution()
    l = []
    li = [[1,4],[4,5]]
    for i in range(len(li)):
        a = Interval(li[i][0], li[i][1])
        l.append(a)
    ans=s.merge(l)
    for i in range(len(ans)):
        print(ans[i].start, ans[i].end)
