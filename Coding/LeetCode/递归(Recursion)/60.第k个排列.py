#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        n_factorial = [0]*(n+1)
        n_factorial[0] = 1
        visited = [False]*(n+1)
        for i in range(1,n+1):
            n_factorial[i] = n_factorial[i-1]*i
        self.ans = str()
 
        def dfs(k,j):#不能将结果变量导入到dfs中去 会产生严重错误!!!
            if j < 0:
                return 
            num_1 =  (k-1)//n_factorial[j] + 1
            num_2 = (k-1)%n_factorial[j] + 1
            value = num_1
            index = 0
            for i in range(1,n+1):
                if visited[i] == False:
                    index += 1
                if index == num_1:
                    value = i
                    break
            visited[value] = True
            self.ans += str(value)
            dfs(num_2,j-1)

        dfs(k,n-1)

        return self.ans
s = Solution()
print(s.getPermutation(3,3))
# @lc code=end


