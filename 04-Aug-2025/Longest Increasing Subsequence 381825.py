# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)