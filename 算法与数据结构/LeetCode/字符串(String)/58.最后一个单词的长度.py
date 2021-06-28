#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left = None
        right = None
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ': #起点
                left = None if left == None else i
            else:
                if left != None:
                    return left - i
        return 0 if left == None else left+1
# @lc code=end

