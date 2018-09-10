class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # o^2 TLE
        # m=0
        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         if i!=j and min(height[i], height[j])*(j-i)>m:
        #             m=min(height[i], height[j])*(j-i)
        # return(m)
        m=0
        i=0;
        j=len(height)-1
        while i<j:
            if min(height[i], height[j])*(j-i)>m:
                m=min(height[i], height[j])*(j-i)
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return(m)

s=Solution()
print(s.maxArea([1, 2, 3, 4]))