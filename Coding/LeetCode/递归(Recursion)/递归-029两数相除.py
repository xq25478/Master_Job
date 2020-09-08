#此题边界有点小问题
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 0:
            return 0
        if divisor == 1 or divisor == -1:
            # if dividend > 2147483647:
            #     dividend = 2147483647
            # if dividend < -2147483647:
            #     dividend = 2147483647
            return dividend if divisor == 1 else -dividend

        sign = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign = -1

        dividend = dividend if dividend>0 else (-dividend)
        divisor = divisor if divisor>0 else (-divisor)
        res = 0        
        while dividend >= divisor:
            a,b= dividend,divisor
            count = 0
            while a >= b:
                dividend = a - b
                b += b
                count = 1 if count == 0 else count+count
            res += count
        return res if sign == 1 else -res
s = Solution()
print(s.divide(9,3))