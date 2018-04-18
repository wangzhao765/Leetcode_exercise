class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 99999999
        maxdiff = 0
        for i in range(len(prices)):
            if prices[i]<min:
                min = prices[i]
            if prices[i]-min>maxdiff:
                maxdiff = prices[i]-min
        return maxdiff

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 6, 4, 3, 1]))