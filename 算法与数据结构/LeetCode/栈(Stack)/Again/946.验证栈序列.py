#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from typing import List
# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed or not popped:return True
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack 
# @lc code=end