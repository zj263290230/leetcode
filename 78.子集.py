#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                dfs(j+1, tmp+[nums[j]])
        
        dfs(0, [])
        return res
        
# @lc code=end

