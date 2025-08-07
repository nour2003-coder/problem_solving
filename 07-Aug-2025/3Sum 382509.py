# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        #[-4,-1,-1,0,1,2]
        for i in range(n-2):
            target=-nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=n-1
            while(j<k):
                sum=nums[k]+nums[j]
                if sum==target:
                    res.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif sum<target:
                    j+=1
                else:
                    k-=1
        return res