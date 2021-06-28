from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #动态规划
        dp = [[[]] if j == 0 else [] for j in range(target+1)]
        for candidate in candidates:
            for j in range(candidate,target+1):
                dp[j] += [res+[candidate] for res in dp[j-candidate]]
        return dp[-1]
s= Solution()
print(s.combinationSum([1,2,3,5],9))
                    


