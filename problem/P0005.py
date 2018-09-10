class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## 这里是O(n^2)的dp
        # l = len(s)
        # value = [[0 for i in range(l)] for j in range(l)]
        # for i in range(l):
        #     value[i][i] = 1
        #
        # m=0
        # x=0
        # y=0
        # for i in range(1, l, 1):
        #     for j in range(0, l-i, 1):
        #         if s[j] == s[j+i] and value[j+1][j+i-1] == i-1:
        #             value[j][j+i]=value[j+1][j+i-1]+2
        #             if value[j][j+i]>m:
        #                 m=value[j][j+i]
        #                 x=j
        #                 y=j+i
        #         else:
        #             value[j][j+i]=value[j][j+i-1]
        # return(s[x:y+1])

        st=":"
        for i in s:
            st = st+"#"+i
        st += "#;"
        l=len(st)
        value=[0 for i in range(l)]

        c=0
        r=0
        mi=0
        for i in range(1,l-1):
            mi=c*2-i
            dif=r-i
            if dif>=0:
                if value[mi]<dif:
                    value[i]=value[mi]
                else:
                    value[i]=dif
                    while st[i+value[i]+1]==st[i-value[i]-1]:
                        value[i] += 1
                    c=i
                    r=i+value[i]
            else:
                value[i]=0
                while st[i + value[i] + 1] == st[i - value[i] - 1]:
                    value[i] += 1
                c = i
                r = i + value[i]
        m=0;
        f=0;
        for i in range(l):
            if value[i]>m:
                m=value[i]
                f=i
        ans=""
        for i in range(f-value[f],f+value[f]+1):
            if st[i]!="#":
                ans += st[i]
        return(ans)


s=Solution()
print(s.longestPalindrome("babad"))