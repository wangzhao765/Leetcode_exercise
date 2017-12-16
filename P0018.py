class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nlist=[]
        l=len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                nlist.append([nums[i]+nums[j],i,j])
        slist=sorted(nlist)
        sl=len(slist)
        p=0;
        q=sl-1;
        ans=[]
        while (p<q):
            if slist[p][0]+slist[q][0]>target:
                q -= 1
            elif slist[p][0]+slist[q][0]<target:
                p += 1
            else:
                pn = p
                while pn<=q and slist[pn][0]==slist[p][0]:
                    pn += 1
                qn = q
                while qn>=p and slist[qn][0]==slist[q][0]:
                    qn -= 1
                for i in range(p,pn):
                    for j in range(q,qn,-1):
                        if (slist[i][1]!=slist[j][1] and slist[i][2]!=slist[j][1] and slist[i][1]!=slist[j][2] and slist[i][2]!=slist[j][2]):
                            temp = sorted([nums[slist[i][1]], nums[slist[i][2]], nums[slist[j][1]], nums[slist[j][2]]])
                            if not temp in ans:
                                ans.append(temp)
                p = pn
                q = qn
        return(ans)


s=Solution()
print(s.fourSum([0,0,0], 0))