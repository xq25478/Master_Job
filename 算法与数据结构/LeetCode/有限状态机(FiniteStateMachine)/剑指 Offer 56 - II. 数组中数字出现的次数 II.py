'''
在一个数组 nums 中除一个数字只出现一次之外，
其他数字都出现了三次。请找出那个只出现一次的数字。
参考链接:有限状态自动机
https://leetcode-cn.com/problems/
shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one,two = 0,0

        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one

        return one