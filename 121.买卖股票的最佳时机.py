#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0:
            return 0
        maxfit = 0
        minPrice = prices[0]
        for i in range(size):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxfit:
                maxfit = prices[i] - minPrice
        
        return maxfit
        
# @lc code=end

