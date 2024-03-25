from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        dp = [[nums[0]]]
        for x in nums[1:]:
            j = len(dp[0]) - 1
            mx = None
            while j >= 0 and mx is None:
                for arr in dp:
                    if j >= len(arr):
                        break
                    if arr[j] % x == 0:
                        mx = arr
                        break
                j -= 1
            j += 1
            if mx is None:
                dp.append([x])
            elif j == len(mx) - 1:
                mx.append(x)
            else:
                dp.append(mx[:(j + 1)] + [x])
            dp.sort(reverse=True, key=lambda a: len(a))
        return max(dp, key=lambda x: len(x))
