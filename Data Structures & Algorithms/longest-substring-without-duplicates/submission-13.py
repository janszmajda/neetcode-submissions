class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, max_l = 0, 0
        d = {}
        for j, value in enumerate(s):
            if value not in d:
                d[value] = j
            else:
                if d[value] + 1 > i:
                    i = d[value] + 1
                d[value] = j
            max_l = max(max_l, j - i + 1)
        return max_l