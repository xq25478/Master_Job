from typing import List
#001 两数之和
class Solution001:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasp_map = {}
        for index,num in enumerate(nums):
            another = target -  num
            if another in hasp_map:
                return [hasp_map[another],index]
            hasp_map[num] = index
        return None
            
if __name__ == '__main__':
    s1 = Solution001()
    print(s1.twoSum([2,2,7,5,1],6))