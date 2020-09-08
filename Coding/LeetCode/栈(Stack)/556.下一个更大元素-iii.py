#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
import heapq
# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr =list(str(n))
        idx = -1
        heap = []
        heapq.heapify(heap)
        value = 0
        for i in range(len(arr)-2,-1,-1):
            heapq.heappush(heap,arr[i+1])
            if arr[i] < arr[i+1]:
                heapq.heappush(heap,arr[i])
                idx = i
                value = arr[i]
                break

        if idx == -1:
            return -1
        else:
            idx1 = idx
            idx2 = idx+1
            flag = False
            for i in range(len(heap)):
                val = heapq.heappop(heap)
                if val > value and flag == False:
                    arr[idx1] = val
                    flag = True
                else:
                    arr[idx2] = val
                    idx2 += 1
                    
        val = int(''.join(arr)) if int(''.join(arr)) <= 2**31-1 else -1
        return val

# @lc code=end
s = Solution()
print(s.nextGreaterElement(115))


