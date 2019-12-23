#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in mapping:
                top_emelent = stack.pop() if stack else '#'

                if mapping[char] != top_emelent:
                    return False
            else:
                stack.append(char)
        
        return not stack
# @lc code=end

