class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        t = num
        ans = []
        ans = Solution.search(self, t%1000, "") + ans
        t = t//1000
        if t>0:
            ans = Solution.search(self, t%1000, "Thousand") + ans
            t = t//1000
        if t>0:
            ans = Solution.search(self, t % 1000, "Million") + ans
            t = t//1000
        if t>0:
            ans = Solution.search(self, t % 1000, "Billion") + ans
            t = t//1000
        if len(ans)>1 and ans[-1]=="Zero":
            del(ans[-1])
        st = ans[0]
        for i in range(1, len(ans)):
            st = st + " " + ans[i]
        return st

    def search(self, num, tail):
        table1 = ["Zero", "One", "Two", "Three", "Four",
                 "Five", "Six", "Seven", "Eight", "Nine",
                 "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                 "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
                 "Twenty"]
        table2 = ["","","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ans = []
        if num//100>0:
            ans.append(table1[num//100])
            ans.append("Hundred")
        if num%100<=20:
            if num==0:
                ans.append("Zero")
            elif num%100>0:
                ans.append(table1[num%100])
        else:
            ans.append(table2[(num%100)//10])
            if (num%100)%10>0:
                ans.append(table1[(num%100)%10])
        if ans == ["Zero"] and not (tail == ""):
            return []
        if tail!="":
            ans.append(tail)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(1000000))