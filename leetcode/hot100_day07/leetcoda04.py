from typing import List

class Solution:
    @classmethod
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, n
        while l <= r:
            i = l + r >> 1
            j = (m + n + 1) // 2 - i

            # 判断当前的分界点是否合理
            # 拿到四个关键点
            nums1_left_max = nums1[i - 1] if i - 1 >= 0 else float('-inf')
            nums2_left_max = nums2[j - 1] if j - 1 >= 0 else float('-inf')
            nums1_right_min = nums1[i] if i != n else float('inf')
            nums2_right_min = nums2[j] if j != m else float('inf')

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                else:
                    return max(nums1_left_max, nums2_left_max)

            elif nums1_left_max > nums2_right_min:
                r = i - 1
            else:
                l = i + 1

        return 0


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    res = Solution.findMedianSortedArrays(nums1, nums2)
    print(f':{res:*>20.9f}')




