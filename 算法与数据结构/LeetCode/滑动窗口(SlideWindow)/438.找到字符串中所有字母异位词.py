#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_win,hash_need = {},{}
        ans = []
        for char in p:
            hash_need[char] = 1 if  char not in hash_need else hash_need[char] + 1

        n = len(s)
        left = right = vaild = 0
        while right < n:
            if s[right] in hash_need:
                hash_win[s[right]] = hash_win[s[right]] + 1 if \
                                     s[right] in hash_win else 1
                if s[right] in hash_need and \
                    s[right] in hash_win and  \
                    hash_win[s[right]] == hash_need[s[right]]:
                    vaild += 1
            right += 1
            
            #更新条件
            while right - left  >= len(p):
                if vaild == len(hash_need):
                    ans.append(left)
                if s[left] in hash_need:
                    if hash_win[s[left]] == hash_need[s[left]]:
                        vaild -= 1
                    hash_win[s[left]]-= 1
                left +=1
        return ans
# @lc code=end
s= Solution()
print(s.findAnagrams('cbaebabacd','abc'))
