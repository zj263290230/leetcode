#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:

    # 贪心算法
    # def maxSubArray(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     curr_sum = max_sum = nums[0]
    #     for i in range(1, size):
    #         curr_sum = max(nums[i], curr_sum + nums[i])
    #         max_sum = max(max_sum, curr_sum)
        
    #     return max_sum

    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        max_sum = nums[0]
        for i in range(1, size):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum


# @lc code=end

