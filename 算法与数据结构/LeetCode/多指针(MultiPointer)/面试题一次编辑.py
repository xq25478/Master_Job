##############LeetCode之面试题##################

#面试题
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        '''
        :type first:str
        :type second:str
        :rtype bool
        '''
        if len(first) < len(second):
            return self.oneEditAway(second,first)
        if abs (len(first) - len(second) ) >=2 :
            return False
        i = j = 0
        edit_count = 0
        while i < len(first) and j < len(second):
            if first[i] != second[j]:
                if len(first) != len(second):
                    j -= 1
                edit_count+=1
                if edit_count > 1:
                    return False
            i += 1
            j += 1
        return True

s = Solution()
print(s.oneEditAway('a','b'))