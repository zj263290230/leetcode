#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        
        dp = [[False for _ in range(size)] for _ in range(size)]
        longest_1 = 1
        res = s[0]

        for r in range(1, size):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_1:
                        longest_1 = cur_len
                        res = s[l:r+1]
            
        
        return res
# @lc code=end

