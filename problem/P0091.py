class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        ans=[]
        ans.append(1)
        if len(s)==1:
            return 1
        t = s[0]+s[1]
        tnum = int(t)
        if tnum<=26:
            ans.append(2)
        else:
            ans.append(1)
        if len(s)==2:
            return ans[1]
        for i in range(2,len(s)):
            t = s[i-1]+s[i]
            tnum = int(t)
            if tnum<=26:
                ans.append(ans[i-1]+ans[i-2])
            else:
                ans.append(ans[i-1])
        return(ans[len(s)-1])


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("121"))