'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

'''
class Solution:
    #思路一 hash
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}

        n = len(nums)
        for i in nums:
            ht[i] = 0 if i not in ht else ht[i] + 1


        for num in ht.keys():
            if ht[num] >= n //2:
                return num
        return None

    '''
    #思路2 数组排序法： 将数组 nums 排序，由于众数的数量超过数组长度一半，
    # 因此 数组中点的元素 一定为众数。此方法时间复杂度 O(Nlog_2N)
    '''

    #思路3  摩尔投票法
        # votes = 0
        # for num in nums:
        #     if votes == 0: x = num
        #     votes += 1 if num == x else -1
        # return x
