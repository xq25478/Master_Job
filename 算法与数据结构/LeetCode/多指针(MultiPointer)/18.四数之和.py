#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from collections import Counter
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        dic = Counter(nums) #对每个数出现的次数进行统计
        arr = sorted(dic.keys())  #排序键值
        for i, a in enumerate(arr):
            dic[a] -= 1 #a用掉了一次，而且a的位置之后不会再遍历到了，不需要加回
            for j, b in enumerate(arr[i:]):  #从arr[i]开始找b的值
                if dic[b] < 1: #b可能等于a，判断一下，如果dic[b]不够1个，跳过这次循环
                    continue
                dic[b] -= 1
                for c in arr[i+j:]:  #从arr[i+j]开始找c的值，注意上一层循环枚举j以后，需要再加最外层的i
                    if dic[c] < 1: #同上层循环b的判断
                        continue
                    d = target - (a + b + c)  
                    if d < c:   #因为是非递减顺序，如果d小于c，就直接跳出，这样就可以避免重复
                        break
                    if (d == c and dic[d] > 1) or (d > c and dic[d] > 0):
                        res.append([a, b, c, d])
                dic[b] += 1 #b现在所处的位置，之后a还会遍历到，因此需要加回1
        return res
# @lc code=end

