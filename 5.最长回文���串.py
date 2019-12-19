#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.83%)
# Likes:    1553
# Dislikes: 0
# Total Accepted:    153.7K
# Total Submissions: 552.1K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    # 暴力解法
    # def __valid(self, s, left, right):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    # def longestPalindrome(self, s: str) -> str:
    #     size = len(s)
    #     if size < 2:
    #         return s

    #     max_len = 1
    #     res = s[0]

    #     for i in range(size):
    #         for j in range(i+1, size):
    #             if j - i + 1 > max_len and self.__valid(s, i, j):
    #                 max_len = j - i + 1
    #                 res = s[i: j + 1]
        
    #     return res

    # 中心扩散法
    # def __center_spread(self, s: str, size: int, left: int, right: int):
    #     i = left
    #     j = right

    #     while i >= 0 and j < size and s[i] == s[j]:
    #         i -= 1
    #         j += 1

    #     return s[i + 1: j]

    # def longestPalindrome(self, s: str) -> str:
    #     size = len(s)
    #     if size < 2:
    #         return s

    #     max_len = 1
    #     res = s[0]

    #     for i in range(size):
    #         str_odd = self.__center_spread(s, size, i, i)
    #         str_even = self.__center_spread(s, size, i, i + 1)

    #         cur_max_str = str_odd if len(str_odd) > len(str_even) else str_even

    #         if len(cur_max_str) > max_len:
    #             max_len = len(cur_max_str)
    #             res = cur_max_str
        
    #     return res

    # dp
    def longestPalindrome(self, s: str) -> str:
        

# @lc code=end

