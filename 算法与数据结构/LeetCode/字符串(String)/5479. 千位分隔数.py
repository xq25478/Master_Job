class Solution:
    def thousandSeparator(self, n: int) -> str:
        if not n:return '0'
        ret = ''
        cnt = 0
        
        while n:
            num = n % 10
            n = n // 10
            ret += str(num)
            cnt += 1
            if cnt % 3 == 0:
                ret += '.'  
                
        n = len(ret)
        
        if ret[-1] == '.':
            ret = ret[n-2::-1]
            
        else:
            ret =  ret[::-1]
        return ret 