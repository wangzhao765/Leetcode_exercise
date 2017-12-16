class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        s = sorted(nums)
        while s[i] + s[j] != target:
            if s[i] + s[j] > target:
                j = j-1
            else:
                i = i+1
        ans = []
        for x in range(len(nums)):
            if nums[x] == s[i] or nums[x] == s[j]:
                ans.append(x)
        return ans

s = Solution()
ans = s.twoSum([3,2,4], 6)
print(ans)

