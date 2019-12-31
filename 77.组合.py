#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrace(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                curr.append(i)
                backtrace(i + 1, curr)
                curr.pop()
        
        output = []
        backtrace()
        return output
        
# @lc code=end

