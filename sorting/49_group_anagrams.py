class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        sort_strs = [("".join(sorted(strs[i])), i) for i in range(n)]
        arr = sorted(sort_strs)
        cur = None
        cur_ind = -1
        ans = []
        for s in arr:
            if s[0] == cur:
                ans[cur_ind].append(strs[s[1]])
            else:
                cur = s[0]
                cur_ind += 1
                ans.append([strs[s[1]]])
        return ans


Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])