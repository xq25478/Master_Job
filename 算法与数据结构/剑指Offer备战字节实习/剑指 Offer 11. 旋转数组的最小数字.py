'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import builtins
from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        '''
        对于有序数组的查找 第一思路便是二分法
        '''
        left = 0
        right = len(numbers)-1
        while left < right:  ## 结束条件
            pivot = left + (right-left)//2
            if numbers[right] > numbers[pivot]:
                right = pivot
            elif numbers[right] < numbers[pivot]:
                left = pivot + 1
            else:
                right -= 1
        return numbers[left]


