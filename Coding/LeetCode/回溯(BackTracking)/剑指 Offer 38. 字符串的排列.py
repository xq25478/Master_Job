'''
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    #剪枝
    def permutation(self, s: str) -> List[str]:
        if not s:return []
        s  = sorted(s) #必须要先排序
        n = len(s)
        res = []
        visited = [False]*n

        
        temp = []
        def backTrack():
            if len(temp) == n:
                res.append(''.join(temp[:]))
                return 

            for i in range(n):
                if visited[i] ==  True:
                    continue

                if i > 0 and s[i] == s[i-1] and visited[i-1] == False:
                    continue

                temp.append(s[i])
                visited[i] = True
                backTrack()
                temp.pop()
                visited[i] = False

        backTrack()
        return res