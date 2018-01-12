class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            if nums[i]==val:
                sum = sum + 1
        for i in range(sum):
            nums.remove(val)
        return sum


if __name__ == '__main__':
    s = Solution()
    a = [1]
    print(s.removeElement(a, 1), a)