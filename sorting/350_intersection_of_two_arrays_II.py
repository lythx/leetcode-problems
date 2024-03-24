from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mn1 = min(nums1)
        mx1 = max(nums1)
        r1 = mx1 - mn1 + 1
        count1 = [0] * r1
        mn2 = min(nums2)
        mx2 = max(nums2)
        r2 = mx2 - mn2 + 1
        count2 = [0] * r2
        for x in nums1:
            count1[x - mn1] += 1
        for x in nums2:
            count2[x - mn2] += 1
        i = max(mn1, mn2)
        ans = []
        while i <= min(mx1, mx2):
            while count1[i - mn1] > 0 and count2[i - mn2] > 0:
                ans.append(i)
                count1[i - mn1] -= 1
                count2[i - mn2] -= 1
            i += 1
        return ans