
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letter_count = ord('Z') - ord('A') + 1
        task_counts = [0] * letter_count
        for t in tasks:
            task_counts[ord(t) - ord('A')] += 1
        arr = [t for t in task_counts if t != 0]
        arr.sort(reverse=True)
        ans = 0

        while arr[0] > 0:
            arr[0] -= 1
            completed = 1
            for i in range(1, len(arr)):
                if arr[i] > 0:
                    arr[i] -= 1
                    completed += 1
                else:
                    arr = arr[:i]
                    break
                if completed == n + 1:
                    arr.sort(reverse=True)
                    break
            if arr[0] > 0:
                ans += n + 1
            else:
                ans += completed
        return ans