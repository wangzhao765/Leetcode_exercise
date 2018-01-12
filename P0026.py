class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        sum = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                nums[sum] = nums[i]
                sum = sum + 1
        return sum

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([]))