'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，
1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字
可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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
        dp_1 = 1 #以s[i]结尾的数字的前i个数字当中最后一个是由一个数字替换
        dp_2 = 0 #以s[i]结尾的数字的前i个数字当中最后一个是由两个数字替换

        for i in range(1,n):
            if 10 <= num_to_list[i-1]*10 + num_to_list[i] <= 25: #
            #dp_1不变
                temp = dp_1
                dp_1 += dp_2
                dp_2 = temp
            else:
                dp_1 += dp_2
                dp_2 = 0

        return dp_2 + dp_1
                