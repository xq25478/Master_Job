#
# @lc app=leetcode.cn id=1163 lang=python3
#
# [1163] 按字典序排在最后的子串
#
'''
假设序列是dcbaaaaadcbaaadcbaa，首先需要筛选第一个字母为d，再筛选第二个字母c，以此类推；
筛选出第1字母d后，记录下字符串中以d开头的子串位置，构成队列，假设共n1个；筛选第2个字母，
在队列中依次取n1个元素，从每个子串位置的下一位置找到最大的字母，添加到队列尾部；
直至最后队列为能有的元素只有1个；

初始化队列时需要注意去重；从第i位置开始形如aaaaaaaaaaaabcde，前面重复same个a（不含第一个a），则添加队列时中间那么多个a，只需要处理i-(same+1)/2的位置添加到队列；

作者：krystalyn
链接：https://leetcode-cn.com/problems/last-substring-in-lexicographical-order/solution/tong-guo-dui-lie-dui-zi-chuan-zhu-ge-sao-miao-shai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def lastSubstring(self, s: str) -> str:
        s_len, left, right, step = len(s), 0, 1, 0
        while(right + step < s_len):
            if s[right + step] > s[left + step]:
                left, right, step = right , right+1, 0
            elif s[right + step] < s[left + step]:
                right, step = right+step+1, 0
            else:
                step += 1
        return s[left:] 
# @lc code=end

