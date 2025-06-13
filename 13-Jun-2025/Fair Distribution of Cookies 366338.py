# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_=[float("inf")]
        def backtrack(l,index):
            if index == len(cookies):
                min_[0]=min(min_[0],max(l))
                return
            for i in range(k):
                l[i]+=cookies[index]
                if max(l)<min_[0]:
                    backtrack(l,index+1)
                l[i]-=cookies[index]
        l=[0 for _ in range(k)]
        backtrack(l,0)
        return(min_[0])