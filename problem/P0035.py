class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
            if i==len(nums)-1:
                return i+1


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3], 4))