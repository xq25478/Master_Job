'''
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5
'''
from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def _mergeSort(arr:List[int],temp:List[int],left:int,mid:int,right:int)->int:
            inv_count = 0
            #arr_copy = arr[:]  #每次申请临时数组极为耗费时间 删除
            #对两个子数组进行排序归并成大数组
            i = left
            j = mid + 1
            k = left
            #数组的两边已经分别有序 只需进行选择排序即可
            while ( i<= mid ) and ( j <= right ):
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                    inv_count += j-mid-1
                else :
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid :
                temp[k] = arr[i]
                k += 1
                i += 1
                inv_count += j-mid-1

            while j <= right:
                temp[k] = arr[j]
                k += 1
                j += 1  

            nums[left:right+1] = temp[left:right+1]
            return inv_count
        #递归式归并排序 自顶向下
        def mergeSortRecursive(arr:List[int],temp:List[int],left:int,right:int):
            inv_count = 0
            if left < right :
                mid = (left+right)//2
                inv_count = mergeSortRecursive(arr,temp,left,mid) + mergeSortRecursive(arr,temp,mid+1,right)
                inv_count += _mergeSort(arr,temp,left,mid,right)

            return inv_count

        if not nums: return 0
        temp = [0]*len(nums)
        return mergeSortRecursive(nums,temp,0,len(nums)-1)