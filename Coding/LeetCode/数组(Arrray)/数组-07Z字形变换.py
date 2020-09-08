class Solution007:
    def convert1(self, s: str, numRows: int) -> str:
        arr_len,num = len(s),0
        res = ['']*arr_len
        if numRows == 1:
            return s
        for i in range(numRows):
            idx = i
            odd = False
            while idx < arr_len:
                res[num] = s[idx]
                num += 1

                if i == numRows-1:
                    odd = False                
                elif i == 0:
                    odd = True
                else:
                    odd = not odd
                    
                if odd == True:
                    idx += 2*(numRows-(i+1))
                else:
                    idx += 2*i
        return "".join(res)

    def convert2(self, s:str, n:int)-> str:
        if n < 2: return s
        res =  ['']*n
        i, flag = 0, -1
        for c in s:
            res[i] += c#顺序把字符加入每个列表中
            #每次处于列的首尾就进行翻转
            if i == 0 or i == n-1:  flag = -flag
            i += flag
        return "".join(res)
a = Solution007()
print(a.convert2("LEETCODEISHIRING",4))
