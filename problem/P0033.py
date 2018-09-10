class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return Solution.bsearch(self, 0, len(nums), nums, target)

    def bsearch(self, l, r, nums, target):
        if (l>r or l>=len(nums) or r<0):
            return -1;
        if (l==r):
            if (nums[l]==target):
                return l
            else:
                return -1
        if (target==nums[(l+r)//2]):
            return (l+r)//2
        elif nums[(l+r)//2]>=nums[0]:
            if (target < nums[(l + r) // 2] and target >= nums[l]):
                return Solution.bsearch(self, l, (l + r) // 2 - 1, nums, target)
            elif (target > nums[(l + r) // 2] or (target < nums[l])):
                return Solution.bsearch(self, (l + r) // 2 + 1, r, nums, target)
        elif nums[(l+r)//2]<nums[0]:
            if (target > nums[(l+r)//2] and target<=nums[-1]):
                return Solution.bsearch(self, (l + r) // 2 + 1, r, nums, target)
            else:
                return Solution.bsearch(self, l, (l + r) // 2 - 1, nums, target)



if __name__ == '__main__':
    s = Solution();
    numbers = [5, 1, 3]
    target = 3
    print(s.search(numbers, target))
