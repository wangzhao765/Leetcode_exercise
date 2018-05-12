class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                sum = sum + 1
        for i in range(len(nums)-sum):
            nums.remove(val)
        return sum


if __name__ == '__main__':
    s = Solution()
    a = [0,1,2,2,3,0,4,2]
    print(s.removeElement(a, 2), a)