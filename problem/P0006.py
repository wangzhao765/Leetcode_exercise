class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        l = numRows * 2 - 2
        list=[]
        for i in range(numRows):
            list.append([])
        r = 0
        for i in range(len(s)//l+1):
            for j in range(numRows):
                if r<len(s):
                    list[j].append(r)
                    r += 1
            for j in range(numRows-2, 0, -1):
                if r<len(s):
                    list[j].append(r)
                    r += 1
            # print(r, r+numRows-2*i, i)
            # r += (numRows-2*i)
        ans=""
        for m in list:
            for n in m:
                ans += s[n]
        return(ans)

s=Solution()
print(s.convert("PAYPALISHIRING", 2))