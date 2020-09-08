from typing import List
import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #排序
        len1 = len(nums1)
        len2 = len(nums2)
        nums1.sort()
        nums2.sort()
        res = []
        index1 = 0
        index2 = 0
        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
        return res

'''
思考:
本题本人在尝试的时候，虽然第一时间想到使用二分法去做，但是错误的使用了同时对两个数组进行二分的错误方法
正确方法应该是只对一个数组进行二分即可。哎，或许这就是five吧
'''   
s = Solution()
print(s.intersect([1,2],[2,1]))
print(s.intersect([1,2,2,1],[2,2]))
print(s.intersect([3,1,2],[1,3]))
print(s.intersect([3,1,2],[1,1]))
print(s.intersect([4,9,5],[9,4,9,8,4]))