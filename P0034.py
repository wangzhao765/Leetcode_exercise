class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [Solution.searchLeft(self, nums, 0, len(nums)-1, target), Solution.searchRight(self, nums, 0, len(nums)-1, target)]

    def searchLeft(self, nums, l, r, target):
        m = (l + r)//2
        if l > r or (l == r and nums[l] != target):
            return -1
        if nums[m]==target:
            if m==0 or nums[m-1]!=target:
                return m
            else:
                return Solution.searchLeft(self, nums, l, m-1, target)
        if nums[m]<target:
            return Solution.searchLeft(self, nums, m+1, r, target)
        if nums[m]>target:
            return Solution.searchLeft(self, nums, l, m-1, target)

    def searchRight(self, nums, l, r, target):
        m = (l + r)//2
        if l > r or (l == r and nums[l] != target):
            return -1
        if nums[m]==target:
            if m==len(nums)-1 or nums[m+1] != target:
                return m
            else:
                return Solution.searchRight(self, nums, m+1, r, target)
        if nums[m]<target:
            return Solution.searchRight(self, nums, m+1, r, target)
        if nums[m]>target:
            return Solution.searchRight(self, nums, l, m-1, target)

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([1], 1))