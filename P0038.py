class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        else :
            s = "1"
            for i in range(n-1):
                s = Solution.nextLine(self, s)
        return s

    def nextLine(self, s):
        index = 0
        ans = ""
        while index<len(s):
            tempIndex = index
            count = 0
            while tempIndex<len(s) and s[tempIndex]==s[index]:
                tempIndex += 1
                count += 1
            ans = ans + str(count) + s[index]
            index = tempIndex
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(7))