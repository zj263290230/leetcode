#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        m, n = x, 0
        while m:
            n = n * 10 + m % 10
            m = m // 10
        
        if x == n:
            return True
        return False
        
# @lc code=end

