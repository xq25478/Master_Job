#待做
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)

        #dp init
        dp = [[False]*(len_p+1) for _ in range(len_s+1)]

        #state trans
        for i in range(len_s+1):
            for j in range(len_p+1):
                if j == 0:
                    dp[i][j] = (i == 0)
                else:
                    if p[j-1]!='*':

                    else:
                        if j >= 2:
                            dp[i][j] |= dp[i][j-2]
                        else:



        #output
        return dp[-1][-1]