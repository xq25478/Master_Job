'''
给你两个正整数 n 和 k，二进制字符串  Sn 的形成规则如下：

S1 = "0"
当 i > 1 时，Si = Si-1 + "1" + reverse(invert(Si-1))
其中 + 表示串联操作，reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）

例如，符合上述描述的序列的前 4 个字符串依次是：

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
请你返回  Sn 的 第 k 位字符 ，题目数据保证 k 一定在 Sn 长度范围以内。
'''
from typing import List
class Solution:
    def findKthBit(self, n: int, k: int) -> str:          
        def invertReverse(x:List[str])->List[str]:
            res = []
            for i in range(len(x)-1,-1,-1):
                if x[i] == '0':
                    res.append('1')
                else:
                    res.append('0')
            return res
        
        dp = ["0"]
        if n == 1:
            return dp[k-1]
        
        for _ in range(1,n+1):
            new_dp = dp + ['1'] + invertReverse(dp)
            dp = new_dp
            
        return dp[k-1]
            