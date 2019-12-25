#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def search_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1
        
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.search_insertion_index(nums, target, True)
        
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        
        return [left_index, self.search_insertion_index(nums, target, False)-1]
        
# @lc code=end

