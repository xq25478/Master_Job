#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_win,hash_need = {},{}

        for char in s1:
            hash_need[char] = 1 if  char not in hash_need else hash_need[char] + 1

        n = len(s2)
        left = right = vaild = 0
        while right < n:
            if s2[right] in hash_need:
                hash_win[s2[right]] = hash_win[s2[right]] + 1 if \
                                      s2[right] in hash_win else 1
                if s2[right] in hash_need and \
                    s2[right] in hash_win and  \
                    hash_win[s2[right]] == hash_need[s2[right]]:
                    vaild += 1
            right += 1
            
            #更新条件
            while right - left >= len(s1):
                if vaild == len(hash_need):
                    return True
                if s2[left] in hash_need:
                    if hash_win[s2[left]] == hash_need[s2[left]]:
                        vaild -= 1
                    hash_win[s2[left]]-= 1
                left +=1
        return False
# @lc code=end
s = Solution()
print(s.checkInclusion("ab",'eidboaoo'))