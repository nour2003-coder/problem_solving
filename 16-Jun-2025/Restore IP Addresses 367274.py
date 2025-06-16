# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def backtrack(start,ip):
            if start == len(s):
                if len(ip) == 4:
                    res.append(".".join(ip))
                return 
            for i in range(start+1,min(len(s)+1,start+4)):
                curr = s[start:i]
                if  (curr.startswith('0') and len(curr) > 1)  or int(curr)>255:
                    continue
                backtrack(i,ip+[curr])

        backtrack(0,[])
        return res
