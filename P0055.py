class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxrange=nums[0]
        for i in range(1, len(nums)):
            if i>maxrange:
                return False
            else:
                maxrange=max(maxrange, i+nums[i])
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([3,2,1,0,4]))