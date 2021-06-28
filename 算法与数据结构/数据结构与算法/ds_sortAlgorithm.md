---
title: 数据结构与算法-排序算法
categories:
- 数据结构与算法
tags:
- 排序算法
---
本文主要介绍若干比较常见的排序算法，对每一种排序算法按照算法原理、性能分析、代码实现这三个角度来讲解。
<!-- more -->
# 冒泡排序(Bubble Sort)
## 算法原理
比较相邻的元素。如果第一个比第二个大，就交换他们两个。对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。针对所有的元素重复以上的步骤，除了最后一个。持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
## 性能分析 
时间复杂度O(n^2)  空间复杂度O(1)  稳定排序  原地排序
## 代码实现
```
def bubbleSort(arr:List[int])->List[int]:
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
```
# 插入排序(Insert Sort)
## 算法原理
从数组第2个元素开始抽取元素，把它与左边第一个元素比较，如果左边第一个元素比它大，则继续与左边第二个元素比较下去，直到遇到不比它大的元素，然后插到这个元素的右边，继续选取第3，4，….n个元素,重复步骤 2 ，选择适当的位置插入。
## 性能分析
时间复杂度：O(n^2)  空间复杂度：O(1)  稳定排序  原地排序
## 代码实现
```
def insertSort(arr:List[int])->List[int]:
    for i in range(1,len(arr)):
        j = i-1
        while (j >= 0) and (arr[j] > arr[i]):
            j -= 1
        temp = arr[i]
        k = i
        while k > j+1:
            arr[k] = arr[k-1]
            k -= 1
        arr[j+1] = temp
    return arr
```
# 堆排序(Heap Sort)
## 算法原理
[二叉堆的定义和特性](https://mp.weixin.qq.com/s?__biz=Mzg2NzA4MTkxNQ==&mid=2247485231&amp;idx=1&amp;sn=8dfdc04bd209fba3077269faabe7c36f&source=41#wechat_redirect)

堆排序就是把堆顶的元素与最后一个元素交换，交换之后破坏了堆的特性，我们再把堆中剩余的元素再次构成一个大顶堆，然后再把堆顶元素与最后第二个元素交换….如此往复下去，等到剩余的元素只有一个的时候，此时的数组就是有序的了。
## 性能分析
时间复杂度：O(nlogn)  空间复杂度：O(1)  非稳定排序  原地排序
## 代码实现
```
def downAdjust(arr:List[int],parent:int,arr_len:int):
    temp = arr[parent]
    child = 2*parent + 1
    
    while child < arr_len:
        if (child+1)<arr_len and arr[child] > arr[child+1]:
            child += 1
        if temp <= arr[child]:
            break
        arr[parent] = arr[child]
        parent = child
        child = 2*parent + 1
    arr[parent] = temp
    return arr      
    
def upAdjust(arr:List[int],arr_len:int):
    child = arr_len - 1
    parent = (child-1)//2
    temp = arr[child]
    
    while child > 0 and temp < arr[parent]:
        arr[child] = arr[parent]
        arr[parent] = temp
        child = parent
        parent = (child-1)//2
    arr[child] = temp
    return arr
    
def buildMinBinaryHeap(arr:List[int]):
    arr_len  = len(arr)
    i = ( arr_len - 2 )//2
    while i >= 0:
        arr = downAdjust(arr,i,arr_len)
        i -= 1
    return arr

def heapSort(arr:List[int]):
    arr_len = len(arr)
    buildMinBinaryHeap(arr) #构建二叉堆
    i = len(arr)-1
    while i >= 1:
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        arr = downAdjust(arr,0,i)
        i -= 1
    return arr
```
# 归并排序(Merge Sort)
## 算法原理
将一个大的无序数组有序，我们可以把大的数组分成两个，然后对这两个数组分别进行排序，之后在把这两个数组合并成一个有序的数组。由于两个小的数组都是有序的，所以在合并的时候是很快的。通过递归的方式将大的数组一直分割，直到数组的大小为 1，此时只有一个元素，那么该数组就是有序的了，之后再把两个数组大小为1的合并成一个大小为2的，再把两个大小为2的合并成4的 ….. 直到全部小的数组合并起来。
## 性能分析
时间复杂度：O(nlogn)  空间复杂度：O(n)  稳定排序  非原地排序
## 代码实现
```
def _mergeSort(arr:List[int],left:int,mid:int,right:int):
    arr_copy = copy.deepcopy(arr)  
    #对两个子数组进行排序归并成大数组
    i = left
    j = mid + 1
    k = left
    while ( i<= mid ) and ( j <= right ):
        if arr_copy[i] < arr_copy[j]:
            arr[k] = arr_copy[i]
            i += 1
        else :
            arr[k] = arr_copy[j]
            j += 1
        k += 1
    while i <= mid :
        arr[k] = arr_copy[i]
        k += 1
        i += 1
    while j <= right:
        arr[k] = arr_copy[j]
        k += 1
        j += 1  
        
#递归式归并排序    
def mergeSortRecursive(arr:List[int],left:int,right:int):
    if left < right :
        mid = (left+right)//2
        mergeSortRecursive(arr,left,mid)
        mergeSortRecursive(arr,mid+1,right)
        _mergeSort(arr,left,mid,right)
    return arr
#非递归式归并排序
def mergeSortUnRecursive(arr:List[int]):
    arr_len = len(arr)
    i = 1
    while i < arr_len :
        left = 0
        mid = left + i -1
        right = mid + 1
        
        while right < arr_len:
            _mergeSort(arr,left,mid,right)
            left = right + 1
            mid = left + i -1
            right = mid + i
        if left < arr_len and mid < arr_len:
            _mergeSort(arr,left,mid,arr_len-1)
        i += i
    return arr
```
# 快速排序(Quick Sort)
## 算法原理
**待更**
## 性能分析
平均时间复杂度：O(nlogn) 空间复杂度：O(1) 稳定排序 原地排序
## 代码实现
```
#单向扫描
def partion_one(arr:List[int],left:int,right:int):
    major = arr[right]
    i = left
    for j in range(i,right):
        if arr[j] < major:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i+1 
    arr[right] = arr[i]
    arr[i] = major
    return i

#双向扫描
def partion_two(arr:List[int],left:int,right:int):
    major = arr[left]
    i = left+1
    j = right
    
    while i < j :
        while arr[i] < major and i < j:
            i += 1
        while arr[j] > major and i < j:
            j -= 1
            
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    arr[left] = arr[j]
    arr[j] = major

    return j
 
def quickSort(arr:List[int],left:int,right:int):
    if left < right:
        center = partion_two(arr,left,right)
        quickSort(arr,left,center-1)
        quickSort(arr,center+1,right)
    return arr
```
# 选择排序(Select Sort)
## 算法原理
第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。选择排序是不稳定的排序方法。
## 性能分析
时间复杂度O(n^2)  空间复杂度O(1)  非稳定排序  原地排序
## 代码实现
```
def selectSort(arr:List[int])->List[int]:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
```
# 希尔排序(Shell Sort)
## 算法原理
**待更**
## 性能分析
时间复杂度：O(nlogn)  空间复杂度：O(1)  非稳定排序  原地排序 
## 代码实现
```
def _shellsort(arr:List[int],h:int,i:int):
#第i个分组的元素在arr数组当中的绝对位置为 arr[k] for ( k = i k< arr_len,k+=h ) arr[i] arr[i+h] arr[...]
    inserted = arr[i]
    k = i - h
    while ( k >= 0) and (inserted < arr[k]):
        arr[k+h] = arr[k]
        k -= h
    arr[k+h] = inserted
    
def shellSort(arr:List[int])->List[int]:
    arr_len = len(arr)
    h = arr_len//2  
    while h > 0:
        #若h为偶数 没有问题 若n为奇数 第一个分组则多出一个元素 对后续排序没有问题
        #分成h组 每组arr_len/h个
        for i in range(h,arr_len): #i代表第i个分组 一共有h个分组
            _shellsort(arr,h,i) #对第i个分组进行插入排序
        h = h//2
    return arr
```
# 桶排序(待更)
# 计数排序
## 算法原理
计数排序是一种适合于最大值和最小值的差值不是不是很大的排序。基本思想：就是把数组元素作为数组的下标，然后用一个临时数组统计该元素出现的次数，例如 temp[i] = m, 表示元素 i 一共出现了 m 次。最后再把临时数组统计的数据从小到大汇总起来，此时汇总起来是数据是有序的。
## 性能分析
时间复杂度：O(n+k)  空间复杂度：O(k)  稳定排序  非原地排序 k为辅助数组的大小
## 代码实现
```
def countSort(arr:List[int]):
    if len(arr) <= 0:
        return None
    min_value  = max_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i

    arr2 = []   
    for i in range(0,max_value-min_value+1):
        arr2.append(0)

    for i in arr:
        arr2[i-min_value]+=1
    num = 0
    for i in  range(len(arr2)):
        k = arr2[i]
        while k >= 1:
            arr[num] = min_value + i
            num += 1
            k -= 1
    return arr
```