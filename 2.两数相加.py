#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def ln2str(l1):
            if l1.next == None:
                return str(l1.val)
            else:
                return str(l1.val) + str(ln2str(l1.next))
    
        def str2ln(str):
            if len(str) == 1:
                return ListNode(int(str))
            else:
                ln_tmp = ListNode(str[0])
                ln_tmp.next = str2ln(str[1:])
                return ln_tmp
        str1 = ln2str(l1)[::-1]
        str2 = ln2str(l2)[::-1]
        str_res = str(int(str1)+int(str2))[::-1]
        return str2ln(str_res)

        
# @lc code=end

