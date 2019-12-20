#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31

        while y != 0:
            res = res * 10 + y % 10
            if res > of:
                return 0
            y //= 10
        return res if x > 0 else -res
        
# @lc code=end

