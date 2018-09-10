class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        l = len(nums)
        return max(Solution.search(self, nums[0:l-1]), Solution.search(self, nums[1:l]))

    def search(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        ans = []
        ans.append(nums[0])
        ans.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            ans.append(max(ans[i-1], nums[i]+max(ans[0:i-1])))
        return max(ans[-1],ans[-2])

if __name__ == '__main__':
    s = Solution()
    print(s.rob([15, 2, 3, 15]))