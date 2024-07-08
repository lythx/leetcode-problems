from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        visited = [False] * n
        visited[0] = True
        last = nums[0]
        i = k
        while True:
            last, nums[i % n] = nums[i % n], last
            if visited[i % n]:
                if visited[(i + 1) % n]:
                    break
                i += 1
                continue
            visited[i % n] = True
            i += k
