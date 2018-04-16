class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum=nums[0]
        sum=nums[0]
        for i in range(1,len(nums)):
            sum=max(sum+nums[i], nums[i])
            maxsum=max(maxsum, sum)
        return maxsum

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))