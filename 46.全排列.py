#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre.copy())
            return 
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                pre.append(nums[i])
                self.dfs(nums, index + 1, pre, used, res)
                used[i] = False
                pre.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []

        if size == 0:
            return res

        used = [False] * size
        self.dfs(nums, 0, [], used, res)
        return res
        

        
# @lc code=end

