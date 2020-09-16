#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 0:
            return []
        ir numRows == 1:
            return  [[1]]
        if numRows == 2:
            return [[1],[1,1]]
            
        ret = [[1],[1,1]]

        for i in range(1,numRows+1):
            if i == 1:

# @lc code=end

