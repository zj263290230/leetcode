#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def __dfs(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])
        
        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        
        candidates.sort()
        path = []
        res = []

        self.__dfs(candidates, 0, size, path, res, target)
        return res
        
# @lc code=end

