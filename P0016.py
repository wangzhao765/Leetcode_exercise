class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        l=len(nums)
        min=abs(target-nums[0]-nums[1]-nums[2])
        p=0
        q=0
        sum=nums[0]+nums[1]+nums[2]
        for i in range(l-2):
            p=i+1
            q=l-1
            while p<q:
                s=nums[i]+nums[p]+nums[q]
                if abs(target-s)<min:
                    min=abs(target-s)
                    sum=s
                if s-target>0:
                    q -= 1
                else:
                    p += 1
        return(sum)




s=Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
