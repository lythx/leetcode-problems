class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        n = len(nums)
        p = min(indexDiff + 1, n)
        arr = [i for i in range(p)]
        arr.sort(key=lambda i: nums[i])
        for j in range(1, p):
            if abs(nums[arr[j]] - nums[arr[j - 1]]) <= valueDiff:
                return True
        for i in range(n - p):
            rm = nums[i]
            l = 0
            r = p - 1
            while l < r:
                m = (l + r) // 2
                if nums[arr[m]] > rm:
                    r = m - 1
                elif nums[arr[m]] < rm:
                    l = m + 1
                else:
                    l = m
                    break
            arr.pop(l)
            add = nums[i + p]
            l = 1
            r = p - 2
            if add > nums[arr[-1]]:
                arr.append(i + p)
                l = p - 1
            elif add < nums[0]:
                arr.insert(0, i + p)
                l = 0
            else:
                while l < r:
                    m = (l + r) // 2
                    if nums[arr[m - 1]] <= add <= nums[arr[m]]:
                        l = m
                        break
                    elif nums[arr[m]] < add:
                        l = m + 1
                    elif nums[arr[m - 1]] > add:
                        r = m
                arr.insert(l, i + p)
            if l > 0 and abs(nums[arr[l - 1]] - nums[arr[l]]) <= valueDiff:
                return True
            if l < p - 1 and abs(nums[arr[l]] - nums[arr[l + 1]]) <= valueDiff:
                return True
        return False
