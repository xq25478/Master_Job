class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        
        n = len(cont)
        if n == 1:
            return [cont[0],1]
        
        def dfs(idx:int)->List[int]:
            if idx == n-1:
                return [1,cont[idx]]
            a,b = dfs(idx+1)
            return [b,a+cont[idx]*b]

        return dfs(0)[::-1]
            
            

