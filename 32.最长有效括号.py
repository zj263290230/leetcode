#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0] * len(s)
        for k in range(1, len(s)):
            if s[k] == ')':
                if s[k-1] == '(':
                    dp[k] = dp[k-2] + 2
                elif k-dp[k-1]-1 >= 0 and s[k-dp[k-1]-1] == '(':
                    dp[k] = dp[k-1] + dp[k-dp[k-1]-2] + 2
                maxans = max(maxans, dp[k])
        return maxans
        
# @lc code=end

