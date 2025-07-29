# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    from collections import defaultdict,deque
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rec=defaultdict(int)
        d=defaultdict(list)
        n=len(recipes)
        for i in range(n):
            for ing in ingredients[i]:
                d[ing].append(recipes[i])
                rec[recipes[i]]+=1
        q=deque()
        res=[]
        for sup in supplies:
            q.append(sup)
        while(q):
            ele=q.popleft()
            for i in d[ele]:
                rec[i]-=1
                if rec[i] ==0:
                    q.append(i)
                    res.append(i)
        return res
