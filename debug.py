from typing import *


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = ""
        if numerator * denominator < 0: # 负数先变成正数处理
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator == denominator:
            return res + "1"   

        int2str = [str(i) for i in range(10)]
       
        ans = {}
        if numerator > denominator:
            res += str(numerator // denominator)
            numerator =  numerator % denominator
            if numerator == 0: # 后面只处理小数部分
                return res
        else:
            res += "0"
        
        res += "."
        m = len(res) - 1
        while numerator and numerator not in ans:
            m += 1
            ans[numerator] = m
            numerator *= 10
            res += int2str[numerator // denominator]
            numerator %= denominator
        
        if numerator in ans:
            res = res[:ans[numerator]] + "(" + res[ans[numerator]:] + ")"
        return res   
s = Solution()
s.fractionToDecimal(1, 6)