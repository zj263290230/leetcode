#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        if sum(nums[:4]) > target:
            return []
        len_nums = len(nums)
        if len_nums <= 3:
            return []
        result = []
        for one in range(len_nums-2):
            for two in range(one+1,len_nums-1):
                start = two + 1
                end = len_nums-1
                while start != end:
                    sum_num = nums[one] + nums[two] + nums[start] + nums[end]
                    if sum_num == target and [nums[one], nums[two], nums[start], nums[end]] not in result:
                        result.append([nums[one], nums[two], nums[start], nums[end]])
                    if sum_num <= target:
                        start += 1
                    elif sum_num > target:
                        end -= 1
        return result

# @lc code=end

