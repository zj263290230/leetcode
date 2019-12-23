#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    
    def merge(self, lists, left, right) -> ListNode:
        if left == right:
            return lists[left]
        
        mid = left +(right - left ) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoList(l1, l2)

    def mergeTwoList(self, l1, l2)-> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoList(l1, l2.next)
            return l2
# @lc code=end

