'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    #思路 简单的动态规划
    def numWays(self, n: int) -> int:
        dp_1 = 1
        dp_2 = 2
        if n == 0:
            return 0

        for _ in range(3,n+1):
            new_dp = dp_1 + dp_2
            dp_1,dp_2 = dp_2,new_dp
            
        return dp_2%1000000007