from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j_nums1, k_nums2 = len(nums1) - 1, m - 1, n - 1
        while k_nums2 >= 0:
            if j_nums1 >= 0 and nums1[j_nums1] > nums2[k_nums2]:
                nums1[i] = nums1[j_nums1]
                j_nums1 -= 1
            else:
                nums1[i] = nums2[k_nums2]
                k_nums2 -= 1
            i -= 1

s = Solution()


def case_4():
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    s.merge(nums1, m, nums2, n)
    c = [1, 2, 3, 4, 5, 6]
    assert (all(c[i] == nums1[i] for i in range(len(nums1))))


def example_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    c = [1, 2, 2, 3, 5, 6]
    assert (all(c[i] == nums1[i] for i in range(len(nums1))))


case_4()
example_1()
