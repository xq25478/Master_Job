#
# @lc app=leetcode.cn id=1432 lang=python3
#
# [1432] 改变一个整数能得到的最大差值
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        def num2Arr(n:int)->List[int]:
            arr = []
            while n:
                arr.append(n%10)
                n = n // 10
            return arr[::-1]
        def arr2Num(arr:List[int])->int:
            #123456
            n = 0
            for i in range(len(arr)):
                n += arr[i]
                n *= 10
            return n // 10

        if num < 10:
            return 8

        arr = num2Arr(num)
        max_arr = arr[:]
        min_arr = arr[:]
        
        for i in range(len(max_arr)):
            if max_arr[i]!=9:
                idx = i
                for i in range(idx+1,len(max_arr)):
                    if max_arr[i] == max_arr[idx]:
                        max_arr[i] = 9
                max_arr[idx] = 9
                break
        max_num = arr2Num(max_arr)

        if min_arr[0] != 1:
            idx = 0
            for i in range(idx+1,len(min_arr)):
                if min_arr[i] == min_arr[idx]:
                    min_arr[i] = 1
            min_arr[0] = 1
        else:
            for i in range(1,len(min_arr)):
                if min_arr[i]!=0 and min_arr[i]!=1:
                    idx = i
                    for i in range(idx+1,len(min_arr)):
                        if min_arr[i] == min_arr[idx]:
                            min_arr[i] = 0
                    min_arr[idx] = 0
                    break      
                
        min_num = arr2Num(min_arr)
        #print(max_num,min_num)
        return max_num-min_num
# @lc code=end

