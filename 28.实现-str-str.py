#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        if size == 0:
            return size
        
        for i in range(len(haystack)):
            substr = haystack[i:i+size]
            if substr == needle:
                return i
        
        return -1

        
# @lc code=end

