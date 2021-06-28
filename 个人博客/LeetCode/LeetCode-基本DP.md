---
title: LeetCode-DP-基本DP
categories:
- 数据结构与算法
- LeetCode
tags:
- 基本DP
- DP
---

## 198 打家劫舍I
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
<!--more-->
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp_0 = 0
        dp_1 = nums[0]
        
        #dp[i]表示偷窃房屋最大号码为i的最大收益
        for i in range(1,len(nums)):
            new_dp = max(dp_1,nums[i]+dp_0)
            dp_0 = dp_1
            dp_1= new_dp

        return dp_1
```

## 剑指Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

```
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0: return 0
        '''
        思路1 动态规划
        '''
        cnt = 1

        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True

        def check_cooridnate(number):
            hundreds = number // 100
            ten = (number-hundreds*100)//10
            last = number%10
            return hundreds + ten + last

        for i in range(m):
            for j in range(n):
                if dp[i][j] == False and check_cooridnate(i) + check_cooridnate(j) <= k:
                    dij = [(-1,0),(0,-1)] #判断上一个足迹是否是true 如果为true必然可以走到
                    for d in dij:
                        new_row = d[0] + i
                        new_col = d[1] + j
                        if 0 <= new_row < m and 0 <= new_col < n and dp[new_row][new_col] == True:
                            dp[i][j] = True
                            cnt+=1
                            break
        return cnt
```

## 剑指Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

```
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        if not grid[0]:return 0

        rows = len(grid)
        cols = len(grid[0])
        dp = [0 for i in grid[0]] #初始化
        for i in range(cols):
            dp[i] = grid[0][0] if i == 0 else dp[i-1] + grid[0][i] 

        for i in range(1,rows):
            for j in range(cols):
               dp[j] = dp[j] + grid[i][j] if j == 0 else grid[i][j] + max(dp[j],dp[j-1])

        return dp[-1]
s = Solution()
print(s.maxValue([[1,3,1],[1,5,1],[4,2,1]]))
```

## 剑指Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，
1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字
可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

```
class Solution:
    #思路 动态规划
    def translateNum(self, num: int) -> int:
        if not num:return 1
        num_to_list = []

        while num > 0:
            val =  num % 10
            num_to_list.append(val)
            num = num // 10
        
        num_to_list = num_to_list[::-1]
        n  = len(num_to_list)

        dp_1 = 1 #结尾由一个数字替换
        dp_2 = 0 #结尾由两个数字替换

        for i in range(1,n):
            if 10 <= num_to_list[i-1]*10 + num_to_list[i] <= 25: # 可以由两个数字替换
            #dp_1不变
                temp = dp_1
                dp_1 += dp_2
                dp_2 = temp
            else:  #不可以两个数字变换
                dp_1 += dp_2
                dp_2 = 0

        return dp_2 + dp_1
```

## 剑指Offer 42 连续最大子数组和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = nums[0]
        res = dp
        for i in range(1,len(nums)):
            if dp < 0:
                dp = nums[i]
            else:
                dp = dp + nums[i]
            res = max(res,dp)
        return res
```

## 322.零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ amount+1 ] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        return -1 if dp[amount] == amount+1 else dp[amount]
```

## 518 零钱兑换II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

```
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[0]*(amount+1) #dp[i]表示凑合成金额为i的硬币组合数
        dp[0] = 1
        for coin in coins: #状态1 #正确写法 将coin放在外面
            for i in range(1,amount+1):#状态2 
                if i < coin:
                    continue
                dp[i] += dp[i-coin]

        return dp[amount]
``` 

## 1014 最佳观光组合
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。

思路: 动态维护Ai+i的最大值

```
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        best = 0
        ans = 0
        for index in range(len(A)):
            ans = max (ans,A[index]-index + A[best]+best)
            if A[best] + best < A[index] + index:#动态维护best值
                best = index
        return ans
```

## 剑指 Offer 14- I. 剪绳子
* 相似题目 343-整数拆分
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

```
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1]*(n+1)
        dp[2] = 1
        dp[1] = 1

        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*dp[i-j],j*(i-j))

        return dp[-1]
```

## 650 只有两个键的键盘
最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：

Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。

Paste (粘贴) : 你可以粘贴你上一次复制的字符。

给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。

```
class Solution:
    def minSteps(self, n: int) -> int:
        
        dp = [float('inf')]*(n+1)

        dp[0] = float('inf')
        dp[1] = 0
        
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                if i%j == 0:
                    dp[i] = min(dp[i],dp[j] + i//j)
        return dp[-1]

s = Solution()
print(s.minSteps(3))
```

## 121 买卖股票的最佳时机
给定一个数组，它的第i个元素是一支给定股票第i天的价格。

如果你最多只允许完成**一笔交易**（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1:
            return 0

        #1. DP Table define dp[i][k] 
        #dp_1 表示第i天在持有股票(k=1)或者dp_0不持有股票(k=0)下的获得的利润

        #2. base case
        dp_0 = 0
        dp_1 = -prices[0]

        #3. state change
        for i in range(1,n):
            # 第i天不持有股票股票的利润 = max(前一天不持有股票+当前不做任何操作,前一天持有股票+当天卖掉股票)
            new_dp_0 = max(dp_0,dp_1+prices[i])
            # 第i天持有股票股票的利润 = max(前一天持有股票+当前不做任何操作,购买当天股票)
            new_dp_1 = max(dp_1,-prices[i])
            dp_0,dp_1 = new_dp_0,new_dp_1

        return max(dp_0,dp_1)
```

## 122 买卖股票的最佳时机II
相对于第121题的变化是可以进行无限次交易

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1:
            return 0

        #表示第i天在持有股票(k=1)或者不持有股票(k=0)下的获得的利润
        #2. base case
        dp_0 = 0
        dp_1 = -prices[0]

        #3. state change
        for i in range(1,n):
            # 第i天不持有股票的利润 = max(前一天不持有股票+当前不做任何操作,前一天持有股票+当天卖掉股票)
            new_dp_0 = max(dp_0,dp_1+prices[i])
            # 第i天持有股票的利润 = max(前一天持有股票+当前不做任何操作,前一天不持有股票+购买当天股票)
            new_dp_1 = max(dp_1,dp_0-prices[i])
            dp_0,dp_1 = new_dp_0,new_dp_1

        return max(dp_0,dp_1)
```

## 123 买卖股票的最佳时机III
只允许进行最多两次交易

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1:
            return 0
        dp_i10,dp_i11,dp_i20,dp_i21 = 0,float('-inf'),0,float('-inf')

        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price) # 第二次交易手中不含股票
            dp_i21 = max(dp_i21, dp_i10 - price) # 第二次交易手中含有股票
            dp_i10 = max(dp_i10, dp_i11 + price) # 第一次交易手中不含股票
            dp_i11 = max(dp_i11, -price)         # 第一次交易手中含有股票
        return dp_i20
```

## 714 买卖股票的最佳时机含手续费
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票

```
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <=1:
            return 0

        dp_0 = 0
        dp_1 = float('-inf')
        
        #3. state change
        for i in range(0,n):
            new_dp_0 = max(dp_0,dp_1+prices[i])
            new_dp_1 = max(dp_1,dp_0-prices[i]-fee)
            dp_0,dp_1 = new_dp_0,new_dp_1
        return max(dp_0,dp_1)
```

## 309 买卖股票的最佳时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if not length:
            return 0

        '''
        dp_0 表示第i天持有股票
        dp_1 表示第i天不持有股票 处于冷冻期
        dp_2 表示第i天不持有股票 不处于冷冻期
        '''

        dp_0 = -prices[0]
        dp_1 = 0
        dp_2 = 0

        for i in range(1,length):
            #第i天持有股票 
            #1.可能是i-1天持有股票 i天不进行操作
            #2.可能是i-1天不持有股票，不处于冷冻期，i天买入
            new_dp_0 = max(dp_0,dp_2-prices[i])
            #第i天不持有股票 处于冷冻期 表明第i天卖出股票
            new_dp_1 = dp_0 + prices[i]
            #第i天不持有股票 不处于冷冻期 表明i-1没有买入 没有卖出
            new_dp_2 = max(dp_1,dp_2)
            dp_0 = new_dp_0
            dp_1 = new_dp_1
            dp_2 = new_dp_2

        return max(dp_1,dp_2)
```

## 264 丑数II
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

```
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i2 = i3 = i5 = 0

        for _ in range (1,n):
            ugly = min(res[i2]*2,res[i3]*3,res[i5]*5)
            res.append(ugly)

            if ugly == res[i2]*2:
                i2+=1
            if ugly == res[i3]*3:
                i3+=1
            if ugly == res[i5]*5:
                i5+=1

        return res[n-1]
```

## 313 超级丑数
本题原理同264 
```
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res = [1]
        l = len(primes)
        nums = [0]*l

        for _ in range (1,n):
            ugly = [res[nums[i]]*primes[i] for i in range(l)]
            min_ugly = min(ugly)
            res.append(min_ugly)
            for i in range(l):
                if min_ugly == res[nums[i]]*primes[i]:
                    nums[i] += 1
        return res[n-1]
```

## 1567 乘积为正数的最长子数组长度
* 相似题目:152 乘积最大子数组
给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

```
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        #动态规划
        pos_mul = 0
        neg_mul = 0
        ret = 0

        for num in nums:
            if num == 0:
                pos_mul = neg_mul = 0
            elif num > 0:
                pos_mul += 1
                if neg_mul > 0:
                    neg_mul += 1
            else:
                temp = neg_mul
                neg_mul = pos_mul + 1
                pos_mul = 0 if temp == 0 else temp + 1 
            
            ret = max(ret,pos_mul)
            
        return ret
```