from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        # 二分分割点
        l, r = 0, n
        while l <= r:
            i = l + r >> 1
            j = (m + n + 1) // 2 - i

            # 验证当前的切割方法是否合法
            n1_lmax = nums1[i - 1] if i > 0 else -float('inf')
            n2_lmax = nums2[j - 1] if j > 0 else -float('inf')
            n1_rmin = nums1[i] if i < n else float('inf')
            n2_rmin = nums2[j] if j < m else float('inf')

            if n1_lmax <= n2_rmin and n2_lmax <= n1_rmin:
                if (m + n) % 2 == 0:
                    return (max(n1_lmax, n2_lmax) + min(n1_rmin, n2_rmin)) / 2
                else:
                    return max(n1_lmax, n2_lmax)
            elif n1_lmax > n2_rmin:
                r = i - 1
            else:
                l = i + 1

        return -1