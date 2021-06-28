#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_win,hash_need = {},{}

        for char in t:
            hash_need[char] = 1 if  char not in hash_need else hash_need[char] + 1

        n = len(s)
        start = left = right = vaild = 0
        length = n + 1

        while right < n:
            if s[right] in hash_need: #如果需要这个字符 
                hash_win[s[right]] = hash_win[s[right]] + 1 if \
                                     s[right] in hash_win else 1

                if s[right] in hash_need and s[right] in hash_win and  \
                    hash_win[s[right]] == hash_need[s[right]]:
                    vaild += 1
                    
            right += 1
            while vaild == len(hash_need):#找到了全部需要的字符
                if right - left  < length:
                    start = left
                    length = right - left 
                if s[left] in hash_need:#开始缩减left至少一个有效字符
                    if hash_win[s[left]] == hash_need[s[left]]:
                        vaild -= 1
                    hash_win[s[left]]-= 1
                left +=1

        return '' if length == n+1 else  s[start:start+length] 
# @lc code=end
s = Solution()
print(s.minWindow('ADOBECODEBANC','ABC'))

