from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mn = min(nums)
        mx = max(nums)
        r = mx - mn + 1
        buckets = []
        for i in range(n):
            buckets.append([])
        for x in nums:
            buckets[int(((x - mn) / r) * n)].append(x)
        s = 0
        bucket_ind = 0
        for i in range(n):
            s += len(buckets[i])
            if s >= n // 2:
                bucket_ind = i
                s -= len(buckets[i])
                break
        # Sort the middle bucket
        buckets[bucket_ind].sort()
        j = (n + 1) // 2 - s
        for i in range(1, n, 2):
            while j >= len(buckets[bucket_ind]):
                bucket_ind += 1
                j = 0
            nums[i] = buckets[bucket_ind][j]
            j += 1
        j = 0
        bucket_ind = 0
        for i in range(0, n, 2):
            while j >= len(buckets[bucket_ind]):
                bucket_ind += 1
                j = 0
            nums[i] = buckets[bucket_ind][j]
            j += 1


