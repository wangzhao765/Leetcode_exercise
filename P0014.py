class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[] or strs==[""]:
            return("")
        slist=sorted(strs)
        n=len(slist)
        l=min(len(slist[0]), len(slist[n-1]))
        i=0;
        while i<l and slist[0][i]==slist[n-1][i]:
            i += 1
        return(slist[0][0:i])



s=Solution()
print(s.longestCommonPrefix(["",""]))