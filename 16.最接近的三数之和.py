#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        if ans >= target:
            return ans
        
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                tmp = nums[i] + nums[start] + nums[end]
                if abs(target - tmp) < abs(target - ans):
                    ans = tmp
                if tmp > target:
                    end -= 1
                elif tmp < target:
                    start += 1
                else:
                    return ans
        
        return ans

# @lc code=end

