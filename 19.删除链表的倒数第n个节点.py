#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        # 记录头指针
        dummpy = ListNode(0)
        dummpy.next = head

        # 快指针
        fast = dummpy
        while n:
            fast = fast.next
            n -= 1
        # 慢指针
        slow = dummpy
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # 删除
        slow.next = slow.next.next

        return dummpy.next

        
# @lc code=end

