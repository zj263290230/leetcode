#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1 = len(nums1)
        l2 = len(nums2)

        imin, imax = 0, l1
        while imin <= imax:
            imid = (imin + imax) // 2
            j = (l1 + l2 - 2*imid) // 2


            if imid > 0 and nums1[imid-1] > nums2[j]:
                imax = imid - 1
            elif imid < l1 and nums1[imid] < nums2[j-1]:
                imin = imid + 1
            else:
                # print(imid, j)
                if imid == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[imid-1]
                else:
                    max_left = max(nums1[imid-1], nums2[j-1])
                
                if imid == l1:
                    min_right = nums2[j]
                elif j == l2:
                    min_right = nums1[imid]
                else:
                    min_right = min(nums1[imid], nums2[j])
                
                if (l1 + l2) % 2:
                    return min_right
                return (max_left + min_right) / 2.0


        
# @lc code=end

