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
        steplist = []
        for i in range(len(intervals)):
            steplist.append([intervals[i].start, "l"])
            steplist.append([intervals[i].end, "r"])
        steplist.sort()
        dellist=[]
        for i in range(len(intervals)):
            if ([intervals[i].start, "l"] in steplist and [intervals[i].end, "r"] in steplist):
                a = steplist.index([intervals[i].start, "l"])
                b = steplist.index([intervals[i].end, "r"])
                a=a+1
                while (a<b):
                    if steplist[a][1]=="l" and (not a in dellist):
                        dellist.append(a)
                    a=a+1
        dellist.sort()
        for i in range(len(dellist)-1,-1,-1):
            del(steplist[dellist[i]])
        l=0
        while (l<len(steplist)):
            r=l+1
            while (r<len(steplist) and steplist[r][1]=="l"):
                r=r+1
            while (r<len(steplist) and steplist[r][1]=="r"):
                r=r+1
            r=r-1
            ans.append(Interval(steplist[l][0], steplist[r][0]))
            l=r+1
        return ans

if __name__ == '__main__':
    s = Solution()
    l = []
    li = [[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]
    for i in range(len(li)):
        a = Interval(li[i][0], li[i][1])
        l.append(a)
    ans=s.merge(l)
    for i in range(len(ans)):
        print(ans[i].start, ans[i].end)
